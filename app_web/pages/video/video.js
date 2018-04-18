// pages/video/video.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    title:'豆瓣热门电影',
    frist_list: [],
    groom: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var self = this
    wx.request({
      url: 'http://localhost:5000/video/frist',
      method: 'GET',
      success: function (response) {
        var list = response.data.hotmovie_data
        var data = []
        for (var i = 0; i < list.length;i++){
          if (i < 6) {
            var obj = {}            
            obj.title = list[i].title
            obj.url = list[i].url
            obj.cover = list[i].cover
            data.push(obj)
          }
        }
        self.setData({
          frist_list: response.data,
          groom: JSON.stringify(data)
        })
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
  
  }
})