<template>
    <div>
        <Back />
        <p> you are in Provider's panel for {{$route.params.orderid}} </p>
    </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import Back from '@/components/Back.vue'
@Component({
    components: {
        Back
    }
})
export default class Button extends Vue {

}
</script>
