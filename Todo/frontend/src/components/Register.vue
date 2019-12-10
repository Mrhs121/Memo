<template>
    <div class="login-container">
        <el-form :model="ruleForm2" :rules="rules2"
         status-icon
         ref="ruleForm2" 
         label-position="left" 
         label-width="0px" 
         class="demo-ruleForm login-page">
            <h3 class="title">注册</h3>
            <el-form-item prop="username">
                <el-input type="text" 
                    v-model="ruleForm2.username" 
                    auto-complete="off" 
                    placeholder="用户名"
                ></el-input>
            </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" 
                        v-model="ruleForm2.password" 
                        auto-complete="off" 
                        placeholder="密码"
                    ></el-input>
                </el-form-item>
             <el-form-item style="width:100%;">
                <el-button type="primary" style="width:100%;" @click="handleRegister" :loading="logining">注册</el-button>
            </el-form-item>
       

            </el-form>
    </div>
</template>

<script>
export default {
    data(){
        return {
            logining: false,
            ruleForm2: {
                username: 'admin',
                password: '123456',
            },
            rules2: {
                username: [{required: true, message: 'please enter your account', trigger: 'blur'}],
                password: [{required: true, message: 'enter your password', trigger: 'blur'}]
            },
            checked: false
        }
    },
    methods: {
        handleRegister(event){
                    this.$refs.ruleForm2.validate((valid) => {
                if(valid){
                    this.logining = true;
        let data = new URLSearchParams()
        data.append('name', this.ruleForm2.username)
        data.append('password', this.ruleForm2.password )
        data.append('csrfmiddlewaretoken','{{ csrf_token  }}')
        console.log("data : "+data)
        const  that = this
        this.$http
          .post('/register/check/', data)
          .then(function (response) {
            console.log(response)
            alert(response.data.msg)
            if (response.data.status === 0) {
                 that.$router.push({path: '/Login'});
            }
          })
          .catch(function (error) {
            console.log(error)
          })
                }else{
                    console.log('error submit!');
                    return false;
                }
            })
        }
    }
};
</script>

<style scoped>
.login-container {
    width: 100%;
    height: 100%;
}
.login-page {
    -webkit-border-radius: 5px;
    border-radius: 5px;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}
label.el-checkbox.rememberme {
    margin: 0px 0px 15px;
    text-align: left;
}
</style>
