<template>
  <div class="popup">
    <el-form :data="form" ref="form" label-width="30%">
      <el-form-item label="id" prop="id">
        <el-input v-model="form.id" placeholder="用户名称"/>
      </el-form-item>
      <el-form-item label="备注" prop="text">
        <el-input v-model="form.text" placeholder="教派"/>
      </el-form-item>

    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="cancel()">取消</el-button>
      <el-button type="primary" @click="sub()">提交</el-button>
    </div>
  </div>
</template>

<script>
    export default {
        name: "popup",
        // 接收父组件传过来数据和函数
        props: {
            form:{
                type:Object,
                dafaule : {
                    id:'',
                    text: '',
                }
            },
            run:{
                Function
            }
        },
        data() {
            return {
            }
        },
        methods: {
             //取消
            cancel() {
                this.$emit('close','');
                // 点击取消触发父组件传过来的事件run，弹出下面的图
                this.run()
            },
            //提交
            sub() {this.$emit('change', '')
            },
        }
    }
</script>
