<template>
  <div>
    <h3 class="mt-0 primary--text">Tour</h3>
    <div class="gridContainer my-2 mr-2" v-if="tour.length < 100">
      <div class="d-flex" v-for="item in tour" :key="item">
        <div class="dot">{{ item }}</div>→
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DisplayTour",
  props: {
    tour: {
      type: Array,
      required: true
    }
  }
};
</script>

<style lang="scss" scoped>
.gridContainer {
  display: flex;
  color: #1976d2;
  max-width: 100%;
  overflow-x: auto;
}

.dot {
  height: 26px;
  width: 26px;
  background-color: white;
  border-radius: 50%;
  border: 1px solid #1976d2;
  display: flex;
  justify-content: center;
}
</style>