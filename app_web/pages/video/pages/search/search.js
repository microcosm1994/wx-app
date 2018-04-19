// pages/video/pages/search/search.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    status: false,
    groom: [],
    result: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      groom:JSON.parse(options.groom)
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
  search: function (event) {
    var self = this
    if (event.detail.value != ' '){
      wx.request({
        url: 'http://localhost:5000/video/search?q=' + event.detail.value,
        method: 'GET',
        success: function (response) {
          var resultList = []
          for (var i = 0; i < response.data.length; i++) {
            if (response.data[i].type == 'movie') {
              resultList.push(response.data[i])
            }
          }
          self.setData({
            status: true,
            result: resultList
          })
        }
      })
    }
  }
})