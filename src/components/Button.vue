<template>
    <div>
        <button> {{ msg }} </button>
    </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
@Component
export default class Button extends Vue {
    @Prop(String) msg!: string 
}
</script>
