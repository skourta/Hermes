<template>
  <v-container>
    <v-card outlined width="100%">
      <v-container class="pt-1">
        <h2 class="mb-1 primary--text">Instance Details</h2>
        <div class="gridContainer">
          <v-text-field
            v-for="key in Object.keys(instance)"
            :key="key"
            v-model="instance[key]"
            outlined
            dense
            flat
            hide-details
            readonly
            color="primary"
            :label="key"
          ></v-text-field>
        </div>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import { ipcRenderer } from "electron";

const instances = [
  {
    name: "burma14",
    cost: 3358
  },
  {
    name: "bays29",
    cost: 2020
  },
  {
    name: "kroA200",
    cost: 26524
  },
  {
    name: "rl1889",
    cost: 316536
  },
  {
    name: "ali535",
    cost: 202310
  },
  {
    name: "berlin52",
    cost: 7542
  }
];
export default {
  name: "InstanceDetails",
  props: {
    value: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      instance: {
        NAME: "",
        TYPE: "",
        COMMENT: "",
        DIMENSION: "",
        EDGE_WEIGHT_TYPE: "",
        EDGE_WEIGHT_FORMAT: "",
        DISPLAY_DATA_TYPE: "",
        OPTIMAL_SOLUTION: ""
      },
      radioGroup: 0
    };
  },
  mounted() {
    ipcRenderer.on("instanceRead", (event, arg) => {
      this.instance = arg;
      const instance = instances.find(
        element => element.name === this.instance.NAME
      );
      if (instance) {
        this.instance.OPTIMAL_SOLUTION = instance.cost;
      }
    });
  },
  watch: {
    value(newValue) {
      ipcRenderer.send("readInstance", newValue);
    }
  }
};
</script>

<style lang="scss" scoped>
.gridContainer {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
</style>