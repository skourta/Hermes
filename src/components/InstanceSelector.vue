<template>
  <v-container class="pt-1">
    <v-card outlined width="100%">
      <v-container class="pt-1">
        <h2 class="primary--text">Choose an Instance</h2>
        <v-radio-group v-model="radioGroup" class="ma-3" hide-details>
          <v-radio :label="`Choose one of our provided Instances`" :value="0"></v-radio>
          <v-col @click="radioGroup = 0">
            <v-select
              :disabled="radioGroup !== 0"
              :items="items"
              outlined
              placeholder="Instance"
              hide-details
              dense
              item-text="name"
              item-value="value"
              v-model="instance"
            ></v-select>
          </v-col>
          <v-radio :label="`Choose your own instance`" :value="1"></v-radio>
          <v-col class="d-flex align-center" @click="radioGroup = 1">
            <v-btn
              :disabled="radioGroup !== 1"
              outlined
              color="primary"
              @click="getInstance"
              style="margin-right:1vw"
            >Browse</v-btn>
            <v-text-field
              :disabled="radioGroup !== 1"
              single-line
              outlined
              dense
              flat
              hide-details
              readonly
              v-model="instance"
            ></v-text-field>
          </v-col>
        </v-radio-group>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import { ipcRenderer, app } from "electron";

export default {
  name: "InstanceSelector",
  props: {
    value: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      instance: "",
      items: [
        {
          name: "burma14",
          value: `${
            process.env.NODE_ENV === "development"
              ? "."
              : app.getAppPath("userData")
          }/Python/datasets/burma14.tsp`
        },
        {
          name: "bays29",
          value: `${
            process.env.NODE_ENV === "development"
              ? "."
              : app.getAppPath("userData")
          }/Python/datasets/bays29.tsp`
        }
      ],
      radioGroup: 0
    };
  },
  methods: {
    getInstance() {
      ipcRenderer.send("readFile", "async ping");
    }
  },
  mounted() {
    ipcRenderer.on("fileRead", (event, arg) => {
      this.instance = arg;
    });
  },
  watch: {
    instance() {
      this.$emit("input", this.instance);
    }
  }
};
</script>

<style lang="sass" scoped>
</style>