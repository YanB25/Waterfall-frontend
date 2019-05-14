<template>
  <el-form :model="form" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
  <el-form-item label="username" prop="username">
    <el-input type="text" v-model="this.username" autocomplete="off" :disabled="true"></el-input>
  </el-form-item>
  <el-form-item label="email" prop="email" >
    <el-input type="text" v-model="form.email" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="phone" prop="phone" :disabled="true">
    <el-input type="text" v-model="form.phone" autocomplete="off"></el-input>
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
  <!-- <el-form-item label="确认密码" prop="checkPass">
    <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="年龄" prop="age">
    <el-input v-model.number="ruleForm.age"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item> -->
</el-form>
  <!-- <el-form-item label="活动时间">
    <el-col :span="11">
      <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
    </el-col>
  </el-form-item>
  <el-form-item label="即时配送">
    <el-switch v-model="form.delivery"></el-switch>
  </el-form-item>
  <el-form-item label="活动性质">
    <el-checkbox-group v-model="form.type">
      <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
      <el-checkbox label="地推活动" name="type"></el-checkbox>
      <el-checkbox label="线下主题活动" name="type"></el-checkbox>
      <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
    </el-checkbox-group>
  </el-form-item>
  <el-form-item label="特殊资源">
    <el-radio-group v-model="form.resource">
      <el-radio label="线上品牌商赞助"></el-radio>
      <el-radio label="线下场地免费"></el-radio>
    </el-radio-group>
  </el-form-item>
  <el-form-item label="活动形式">
    <el-input type="textarea" v-model="form.desc"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">立即创建</el-button>
    <el-button>取消</el-button>
  </el-form-item> -->
</el-form>
</template>

<script lang="ts">

interface Callback {
    (err?: Error): any
};

import { Vue, Component, Prop } from 'vue-property-decorator'
@Component
export default class Button extends Vue {
    @Prop(Number) userid?: Number;
    @Prop(String) username?: String;
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
    onSubmit() {
        console.log('submit');
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
        let hasAt = false;
        for (let i = 0; i < value.length; ++i) {
            if (value[i] === '@') {
                hasAt = true;
            }
        }
        if (hasAt) {
            callback();
        } else {
            callback(new Error("not a valid email"));
        }
    }
    checkPhone(rule: Object, value : string, callback: Callback) {
        for (let i = 0; i < value.length; ++i) {
            if (value[i] < '0' || value[i] > '9') {
                callback(new Error('invalid phone number'));
                return;
            }
        }
        callback();
    }
}
</script>
