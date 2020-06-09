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
        DISPLAY_DATA_TYPE: ""
      },
      radioGroup: 0
    };
  },
  mounted() {
    ipcRenderer.on("instanceRead", (event, arg) => {
      this.instance = arg;
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