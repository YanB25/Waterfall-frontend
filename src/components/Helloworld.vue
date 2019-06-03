<template>
  <el-carousel height="200px" direction="vertical" :autoplay="false">
    <el-carousel-item v-for="item in 3" :key="item">
      <h3 class="medium">{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
@Component
export default class Button extends Vue {}
</script>

<style>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  /* background-color: #99a9bf; */
  background-image: url(http://www.daveyslocker.com/wp-content/uploads/2015/04/sunset2.jpg);
}

.el-carousel__item:nth-child(2n + 1) {
  /* background-color: #d3dce6; */
  background-image: url(http://www.daveyslocker.com/wp-content/uploads/2015/04/sunset2.jpg);
}
</style>