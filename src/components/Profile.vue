<template>
  <el-form :model="form" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm" v-loading="isloading">
  <el-form-item label="username" prop="username">
    <el-input type="text" v-model="this.username" autocomplete="off" :disabled="true"></el-input>
  </el-form-item>
  <el-form-item label="email" prop="email" >
    <el-input type="text" v-model="form.email" autocomplete="off" @change="changed"></el-input>
  </el-form-item>
  <el-form-item label="phone" prop="phone" :disabled="true">
    <el-input type="text" v-model="form.phone" autocomplete="off" @change="changed"></el-input>
  </el-form-item>
  <el-form-item label="balance" prop="balance" >
    <el-input type="text" v-model.number="form.balance" autocomplete="off" :disabled="role != 'manager'"></el-input>
  </el-form-item>
  <el-form-item label="role" prop="role" >
    <el-input type="text" v-model="form.role" autocomplete="off" :disabled="role != 'manager'"></el-input>
  </el-form-item>
  <el-form-item label="status" prop="status" >
    <el-input type="text" v-model="form.status" autocomplete="off" :disabled="role != 'manager'"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit('ruleForm')" :disabled="!hasChanged || !emailValid || !phoneValid"> Update </el-button>
  </el-form-item>
</el-form>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';
import validator from 'validator';

interface Callback {
    (err?: Error): any
};

interface LoginComponent extends Vue{
  resetFields(): void,
  validate(valid: object): boolean
}

@Component
export default class Button extends Vue {
    role: string = '';
    isloading: boolean = true;

    userid: number = -1;
    username: string = '';
    hasChanged: Boolean = false;
    emailValid: Boolean = true;
    phoneValid: Boolean = true;

    form = {
        email: '',
        phone: '',
        balance: '',
        role: '',
        status: '',
    };
    rules = {
        email: [
            { validator: this.checkEmail, trigger: 'blur' }
        ],
        phone: [
            { validator: this.checkPhone, trigger: 'blur' }
        ]
    }
    onSubmit(formName: string) {
        (this.$refs[formName] as LoginComponent).validate((valid: any) => {
            if (valid) {
                fetch(`/api/user/${this.userid}`, {
                    method: "POST",
                    body: JSON.stringify(this.form)
                }).then(res => res.json())
                .then(res => {
                    if (res.code === 0) {
                        this.$message({
                            message: "successfully update profile",
                            type: "success"
                        })
                        this.hasChanged = false;
                    } else {
                        this.$message({
                            message: `update fail: ${res.msg}`,
                            type: "error"
                        });
                    }
                })
            } else {
                this.$message({
                    message: "validation error",
                    type: "error"
                });
                return false;
            }
        });
    }

    beforeMount() {
        console.log('mount');
        this.role = sessionStorage.getItem('role') as string;
        if (sessionStorage.getItem('userid')) {
            this.userid = parseFloat(sessionStorage.getItem('userid') as string);
            this.username = sessionStorage.getItem('username') as string;
        }
        fetch(`/api/user/${this.$route.params.userid}`, {
            method: 'GET',
        }).then(res => {
            return res.json();
        }).then(data => {
            if (data.code === 0) {
                console.log(data.data);
                this.form.email = data.data.email;
                this.form.phone = data.data.phone;
                this.form.balance = (data.data.balance as number).toString();
                this.form.role = data.data.role;
                this.form.status = (data.data.status as number).toString();
                console.log(this.form.balance);
            } else {
                this.$message({
                    message: `err: ${data.msg}`,
                    type: "error"
                });
            }
        }).catch(err => {
            this.$message({
                message: `err`,
                type: "error"
            })
        }).finally(() => {
            this.isloading = false;
        })
    }

    checkEmail(rule: Object, value : string, callback: Callback) {
        if (!validator.isEmail(value)) {
            return callback(new Error('Plase enter valid email'));
        }
        callback();
    }
    checkPhone(rule: Object, value : string, callback: Callback) {
        if (!validator.isMobilePhone(value, 'any')) {
            callback(new Error('Plase enter valid phone number'));
        }
        callback();
    }
    changed() {
        this.hasChanged = true;
    }
}
</script>
