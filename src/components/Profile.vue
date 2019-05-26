<template>
  <el-form :model="form" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
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
    <el-input type="text" v-model="form.balance" autocomplete="off" :disabled="true"></el-input>
  </el-form-item>
  <el-form-item label="role" prop="role" >
    <el-input type="text" v-model="form.role" autocomplete="off" :disabled="true"></el-input>
  </el-form-item>
  <el-form-item label="status" prop="status" >
    <el-input type="text" v-model="form.status" autocomplete="off" :disabled="true"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')" :disabled="!hasChanged || !emailValid || !phoneValid"> Update </el-button>
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
    @Prop(Number) userid?: Number;
    @Prop(String) username?: String;
    hasChanged: Boolean = false;
    emailValid: Boolean = true;
    phoneValid: Boolean = true;

    form = {
        email: '',
        phone: '',
        balance: 0,
        role: '',
        status: 0,
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
                alert('submit!');
            } else {
                return false;
            }
        });
    }

    beforeMount() {
        console.log('mount');
        if (this.userid == -1) {
            this.$router.push('/');
        } else {
            fetch(`/api/user/${this.userid}`, {
                method: 'GET',
            }).then(res => {
                return res.json();
            }).then(data => {
                if (data.code === 0) {
                    console.log(data.data);
                    this.form.email = data.data.email;
                    this.form.phone = data.data.phone;
                    this.form.balance = data.data.balance;
                    this.form.role = data.data.role;
                    this.form.status = data.data.status;
                } else {
                    alert(`err: ${data.msg}`)
                }
            })
        }
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
