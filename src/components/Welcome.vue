<template>
<div>
    <el-row :gutter="12">
        <el-col :span="8">
            <el-card shadow="always">
                <i class="hint-icon el-icon-document"></i>
                <span class="hint-text" >Actived Order</span>
                <span class="hint-num">99</span>
            </el-card>
        </el-col>
        <el-col :span="8">
            <el-card shadow="always">
                <i class="hint-icon el-icon-document-checked"></i>
                <span class="hint-text" >Finished Order</span>
                <span class="hint-num">99</span>
            </el-card>
        </el-col>
        <el-col :span="8">
            <el-card shadow="always">
                <i class="hint-icon el-icon-money"></i>
                <span class="hint-text" >Balance</span>
                <span class="hint-num">99</span>
            </el-card>
        </el-col>
    </el-row>
    <br/>
    <el-row :gutter="12">
        <el-col :span="12">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span class="hint-text"> Finish Rate</span>
                </div>
                <div class="box-content graph">
                    <el-progress type="circle" :width="300" :stroke-width="30" :percentage="30"></el-progress>
                    <p>33 Finished / 99 Actived</p>
                </div>
            </el-card>
        </el-col>
        <el-col :span="12">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span class="hint-text">Latest Orders</span>
                    <el-button class="view-more" type="text">View More ></el-button>
                </div>
                <div class="box-content">
                    
                </div>
            </el-card>
        </el-col>
    </el-row>
    <br/>
    <el-row :gutter="12">
        <el-col :span="24">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span class="hint-text"> Shortcuts</span>
                </div>
                <div>
                    <el-button icon="el-icon-tickets">Orders</el-button>
                    <el-button icon="el-icon-user">Profile</el-button>
                    <el-button icon="el-icon-setting">Control Panel</el-button>
                </div>
            </el-card>
        </el-col>
    </el-row>
</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
export default class Button extends Vue {
    
}
</script>

<style>
    .hint-icon {
        font-size: 80px;
        color: #409EFF;
    }
    .hint-text {
        font-size: 24px;
        color: #CCC;
    }
    .hint-num {
        float: right;
        font-size: 75px;
        color: #409EFF;
    }
    .view-more {
        float: right;
        padding: 0px;
        line-height: 24px;
    }
    .box-content {
        height: 400px;
        padding: 20px;
    }
    .graph {
        text-align: center;
    }
    .graph > p {
        height: 60px;
        line-height: 60px;
        font-size: 18px;
        color: #CCC;
    }
</style>

