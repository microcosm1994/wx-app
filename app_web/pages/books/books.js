// pages/books/books.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    free: [],
    wrap: [],
    week: [],
    writer: [],
    zindex: [false, true, true]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var self = this
    wx.request({
      url: 'http://localhost:5000/book/wrap',
      method: 'GET',
      success: function (response) {
        if (response.statusCode == 200) {
          console.log(response)
          self.setData({
            wrap: response.data
          })
        }
      }
    })
    wx.request({
      url: 'http://localhost:5000/book/free',
      method: 'GET',
      success: function (response) {
        if (response.statusCode == 200){
          console.log(response)
          self.setData({
            free: response.data
          })
        }
      }
    })
    wx.request({
      url: 'http://localhost:5000/book/week',
      method: 'GET',
      success: function (response) {
        if (response.statusCode == 200) {
          console.log(response)
          self.setData({
            week: response.data
          })
        }
      }
    })
    wx.request({
      url: 'http://localhost:5000/book/writer',
      method: 'GET',
      success: function (response) {
        if (response.statusCode == 200) {
          console.log(response)
          self.setData({
            writer: response.data
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
  curent: function () {
    var arr = this.data.zindex
    arr.unshift(arr.pop())
    this.setData({
      zindex: arr
    })
  }
})