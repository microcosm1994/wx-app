// pages/books/detailed/detailed.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    url: '',
    info: {},
    content: {},
    height: '1210rpx',
    isshow: false,
    list: {},
    list_show: true,
    loading_show: false,
    detaild_loading_show: false
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options.url)
    this.setData({
      url: options.url
    })
    var self = this
    wx.request({
      url: 'http://localhost:5000/book/detailed?url=' + options.url,
      method: 'GET',
      success: function (response) {
        if (response.statusCode == 200) {
          self.setData({
            info: response.data,
            detaild_loading_show: true
          })
        }
      }
    })
    wx.request({
      url: 'http://localhost:5000/book/detailed_read?type=try&url=' + options.url,
      method: 'GET',
      success: function (response) {
        if (response.statusCode == 200) {
          self.setData({
            content: response.data,
            detaild_loading_show: true
          })
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  },
  show: function () {
    this.setData({
      height:'auto',
      isshow: true
    })
  },
  listshow: function () {
    var self = this
    console.log(self.data.url)
    this.setData({
      list_show: false
    })
    wx.request({
      url: 'http://localhost:5000/book/detailed_list?url=' + self.data.url,
      method: 'GET',
      success: function(response) {
        if (response.statusCode == 200) {
          console.log(response.data == '')
          console.log(response.data.length)
          if (response.data != '') {
            self.setData({
              list: response.data,
              loading_show: true
            })
          } else{
            var message = [{
              title: '获取目录失败',
              content: [{
                title: '可能由于页面数据动态生成，爬虫无法获取'
              }]
            }]
            self.setData({
              list: message,
              loading_show: true
            })
          }
          console.log(self.data.list)
        }
      }
    })
  },
  listclose: function () {
    this.setData({
      list_show: true
    })
  }
})