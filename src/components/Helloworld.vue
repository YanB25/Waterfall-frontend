<template>
  <div>
    <el-row>
      <el-col :offset="2"  :span="24">
        <div class="main-logo">
          <img src="static/logo_main.png" />
          <br/>
          <p>Efficient / Fresh / Crowdsourcing</p>
          <p>Joining us by hitting the "Sign Up" Button</p>
        </div>
        <el-row>
          <el-row :gutter="12">
            <el-col :span="8">
              <el-card shadow="always">
                <el-image
                   class="card-pic"
                  src="https://cdn.pixabay.com/photo/2016/07/03/22/36/transportation-1495618_960_720.jpg"
                  fit="cover">
                </el-image>
                <div class="card-text">
                  <span>Efficient</span>
                  <div class="bottom clearfix">
                    xxxxxxxxxxxxxxxxxxxxxxxx
                  </div>
                </div>
              </el-card>
            </el-col>
            <el-col :span="8">
              <el-card shadow="always">
                <el-image
                   class="card-pic"
                  src="https://cdn.pixabay.com/photo/2018/10/06/11/48/north-sea-3727730_960_720.jpg"
                  fit="cover">
                </el-image>
                <div class="card-text">
                  <span>Fresh</span>
                  <div class="bottom clearfix">
                    xxxxxxxxxxxxxxxxxxxxxxxxxx
                  </div>
                </div>
              </el-card>
            </el-col>
            <el-col :span="8">
              <el-card shadow="always">
                <el-image
                   class="card-pic"
                  src="https://cdn.pixabay.com/photo/2016/06/09/09/52/hands-1445472_960_720.jpg"
                  fit="cover">
                </el-image>
                <div class="card-text">
                  <span>Crowdsourcing</span>
                  <div class="bottom clearfix">
                    xxxxxxxxxxxxxxxxxxxxxxxxxx
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </el-row>
      </el-col>
    </el-row>
  </div>
  
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
@Component
export default class Button extends Vue {}
</script>

<style>
  .main-logo {
    text-align: center;
  }
  .main-logo p {
    font-size: 24px;
    color: #409EFF;
  }
  .card-text{
    padding: 14px;
  }
  .card-text > span {
    font-size: 24px;
    color: #409EFF;
  }
  .card-pic {
    height: 400px;
    width: 100%;
  }
</style>