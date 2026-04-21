<template>
  <div id="page">
    <div id="avatar"></div>

    <div id="information">
      <p class="title_text">User Information:</p>
      <p class="label_text">Name:</p>
      <span class="info_text">{{ name }}</span>

      <p class="label_text">Age:</p>
      <span class="info_text">{{ age }}</span>

      <p class="label_text">Email:</p>
      <span class="info_text">{{ email }}</span>

      <p class="label_text">Phone:</p>
      <span class="info_text">{{ phone }}</span>

      <p class="label_text">Address:</p>
      <span class="info_text">{{ address }}</span>
    </div>

    <div id="buttons"></div>
  </div>
</template>

<script setup lang="ts">
const name = "Hesse"
const age = "15"
const email = "14235235@535@cog.con"
const phone = "1231415151"
const address = "1241 setsf St. tihSth. TX, 543536"



</script>

<style lang="css"></style>
