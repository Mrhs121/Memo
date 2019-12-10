<template>
  <div class="login">
    <div>
      <el-input placeholder="请输入用户名" v-model="name" clearable class="input_style"></el-input>
      <span v-if="error.name" class="err-msg">{{error.name}}</span>
    </div>
    <div>
      <el-input placeholder="请输入密码" v-model="pwd" show-password class="input_style"></el-input>
      <span v-if="error.pwd" class="err-msg">{{error.pwd}}</span>
    </div>
    <div>
      <el-button type="primary" @click="login" class="login_style">登录</el-button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Login",
    data(){
      return {
        name: '',
        pwd : '',
        error : {
          name: '',
          pwd : ''
        }
      }
    },
    methods:{
      login(){
        const { name, pwd, $router} = this
        this.$router.push({
          name: "Main",
          params: {
            username: this.name
          }
        });
      }
    }
  }
</script>

<style>
  .login{
    margin-top: 200px;
  }
  .input_style{
    width: 200px;
    margin-bottom: 10px;
  }
  .login_style{
    width: 200px;
  }
</style>
