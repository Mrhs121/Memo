<template>




  <div class="content">

    <h1 style="color: #000035">云端备忘录</h1>
    <h5>随时随地记录重要信息</h5>

    <textarea style="width: 100%;height:100px;
    line-height:30px;
    text-align: center;font-size: 15px;
    color: #8c939d;
    margin-top: 8px;
    display: table-cell; vertical-align: middle;
    border-top-right-radius:10px;border-top-left-radius:10px;border-bottom-left-radius:10px;border-bottom-right-radius:10px;" v-model="msg"></textarea>
    <el-button type="primary" style="border: 1px solid #000;color: #000;width:100%;margin-top:4px;background:white;" @click="handleSubmit">提交</el-button>

     <!--<div class="main">-->
        <!--<dialog-bar v-model="contents" v-model="sendVal" type="confirm" title="修改便签" content= {{ contents }}  v-on:cancel="clickCancel()" @danger="clickDanger()" @confirm="clickConfirm()"></dialog-bar>-->
    <!--</div>-->

      <el-row style="margin-top: 20px">
        <el-table :data="todolist" style="border: 2px solid #000;width: 100%; border-top-right-radius:15px;border-top-left-radius:15px;border-bottom-left-radius:15px;border-bottom-right-radius:15px;
  " border>

          <el-table-column prop="id" label="id" width="40px">
            <template slot-scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>

          <el-table-column prop="text" label="便签" min-width="35%">
            <template slot-scope="scope"> {{ scope.row.fields.text }} </template>
          </el-table-column>

          <el-table-column prop="add_date" label="添加时间" min-width="20%">
            <template slot-scope="scope"> {{ scope.row.fields.add_date }} </template>
          </el-table-column>



          <el-table-column  label="操作" width="170px" style="align-content: center">
             <template slot-scope="scope"  >
              <el-button  type="primary" @click="del(scope.row.pk)" style="border: red;float:left; margin: 2px; background: red" >删除</el-button>
              <el-button type="primary" @click="edit(scope.row.pk,scope.row.fields.text)" style="float:left; margin: 2px;">修改</el-button>
             </template>
          </el-table-column>

        </el-table>

     </el-row>
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
        dialogFormVisible: false,
        contents:'hello',
        sendVal: false,
        dialogVisible: false,
        msg: '今天做点什么呢？',
        checked: false,
        todolist: []
      }
    },
    mounted: function() {
      this.showTodolist()
    },
    methods: {


      handleSubmit(event) {
            this.logining = true;
            let data = new URLSearchParams()
            data.append('data', this.msg)
            data.append('csrfmiddlewaretoken', '{{ csrf_token  }}')
            console.log("data : " + data)
            const that = this
            this.$http
              .post('/info/', data)
              .then(function (response) {
                console.log(response)
                if (response.data.status === 0) {
                  that.reload()
                }
              })
              .catch(function (error) {
                console.log(error)
              })

      },
      showTodolist(){
             this.$http.get('/info/').then((response) => {
               console.log(response)
            // var res = JSON.parse(response.data)
            console.log(response.data.list)
            if (response.data.status === 0) {
              this.todolist = response.data.list
              console.log("get list success")
            } else {
              // console.log(res['msg'])
              console.log("not get list")
            }
        })
      },
      del(id){
            let data = new URLSearchParams()
            data.append('id', id)
            data.append('csrfmiddlewaretoken', '{{ csrf_token  }}')
            const that = this
             this.$http.post('/del/',data).then((response) => {
               console.log(response)
                 this.reload()

        })
      },
      edit(id,text){
        console.log("传递参数："+text)
          this.$router.push({
            path:'/Modify',
            query: { id: id ,text:text}
            },
          )
        //     let data = new URLSearchParams()
        //     data.append('id', id)
        //     data.append('text', text)
        //     data.append('csrfmiddlewaretoken', '{{ csrf_token  }}')
        //     const that = this
        //      this.$http.post('/edit/',data).then((response) => {
        //        console.log(response)
        //          this.reload()
        // })
      },
      showBg(id) {
        $("#btnVal").val(id);
        $(".mask").show();
        $(".edit").show();
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
    border: 4px solid #000;
    padding: 20px;
    border-top-right-radius:20px;border-top-left-radius:20px;border-bottom-left-radius:20px;border-bottom-right-radius:20px;
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


