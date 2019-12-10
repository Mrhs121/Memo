<template>

  <div class="content">

    <h1>修改便签</h1>

    <textarea rows="5" style="width: 100%;height:200px;font-size: 16px; margin-top: 2px;display: table-cell; vertical-align: middle" v-model="text"></textarea>
    <div style=" display: flex;">
      <el-button type="primary" style="width:50%;margin-top: 4px" @click="edit">修改</el-button>
      <el-button type="primary" style="width:50%;margin-top: 4px" @click="cancel">取消</el-button>
    </div>


  </div>



</template>

<script>
import dialogBar from './mydialog.vue'
import popup from './popup.vue'

  export default {
    inject:['reload'],
    components:{
        'dialog-bar': dialogBar,
        popup
    },
    data() {
      return {
        id : '',
        dialogFormVisible: false,
        contents:'hello',
        sendVal: false,
        dialogVisible: false,
        text: '今天做点什么呢？',
        checked: false,
      }
    },
    created() {
            console.log("created 获得参数："+this.$route.query.id+" "+this.$route.query.text)
            this.id = this.$route.query.id;
            this.text = this.$route.query.text;
    },
    watch: {
      // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
      '$route': 'getParams'
    },
    methods: {
      getParams(){
            console.log("getParams 获得参数："+this.$route.query.id+" "+this.$route.query.text)
            this.id = this.$route.query.id;
            this.text = this.$route.query.text;
      },
      edit(){
            let data = new URLSearchParams()
            data.append('id', this.id)
            data.append('text', this.text)
            data.append('csrfmiddlewaretoken', '{{ csrf_token  }}')
            const that = this
             this.$http.post('/edit/',data).then((response) => {
               console.log(response)
              this.$router.go(-1);
        })
      },
      cancel(){
              this.$router.go(-1);
        }



    }
  };
</script>


<style lang="less" scoped>


  * {
    padding: 0;
    margin: 0 auto;
    /*margin: 0;*/
  }

  body {
    width: 100%;
    height: 100%;
  }

  .content {
    height: 100%;
    width: 60%;
    background: rgb(249, 249, 249);
    border: 2px solid #000;
    padding: 20px;
    border-top-right-radius:15px;border-top-left-radius:15px;border-bottom-left-radius:15px;border-bottom-right-radius:15px;
  }


  .text {
    height: 150px;
    width: 450px;
    color: rgb(255, 255, 255);
    font-size: 18px;
    line-height: 25px;
    float: left;
    resize: none;
    padding-left: 5px;
    border-radius: 10px;
  }

  .btn {
    width: 80px;
    height: 40px;
    background: #428bca;
    border: 0;
    float: left;
    margin-top: 55px;
    margin-left: 8px;
    border-radius: 10px;
  }

  .btn a {
    text-decoration: none;
    color: black;
    line-height: 80px;
  }

  .info {
    margin-top: 4px;
    height: 100px;
    width: 100%;
    background: #FFF;
    float: left;
    border: 1px solid #000;
    border-radius: 10px;
  }

  .info p {
    word-break: break-all;
    width: 400px;
    height: 85px;
    float: left;
    overflow: hidden;
    white-space: normal;
    cursor: pointer;
    padding: 5px;
  }

  .info .btn {
    width: 60px;
    height: 40px;
    background: #428bca;
    border: 0;
    float: left;
    margin: 5px 0 0 1px;
    border-radius: 10px;
  }

  .mask {
    position: absolute;
    top: 0px;
    filter: alpha(opacity=60);
    background: #777;
    z-index: 100;
    left: 0px;
    opacity: 0.5;
    -moz-opacity: 0.5;
    width: 100%;
    height: 100%;
    display: none;
  }

  .edit {
    background-color: #fff;
    border: 5px solid rgba(0, 0, 0, 0.4);
    height: 233px;
    left: 50%;
    margin: -200px 0 0 -200px;
    padding: 1px;
    position: fixed !important; /* 浮动对话框 */
    position: absolute;
    top: 50%;
    width: 400px;
    z-index: 101;
    border-radius: 5px;
    display: none;
  }

  .edit p {
    margin: 0 0 12px;
    height: 24px;
    background: #CCCCCC;
    font-size: 18px;
    line-height: 25px;
    padding-left: 5px;
  }

  .edit p.close {
    text-align: right;
    padding-right: 10px;
  }

  .edit p.close a {
    color: #fff;
    text-decoration: none;
  }

  .text1 {
    height: 150px;
    width: 398px;
    color: #999;
    font-size: 18px;
    line-height: 25px;
    float: left;
    resize: none;
    border-radius: 10px;
  }

  .btn1 {
    width: 80px;
    height: 40px;
    background: #428bca;
    border: 0;
    float: left;
    border-radius: 10px;
    margin-left: 151px;
    margin-top: 3px;
  }

  .infos {
    /*height: 550px;*/
  }

  .pagination {
    float: left;
    margin-top: 6px;
  }
</style>


