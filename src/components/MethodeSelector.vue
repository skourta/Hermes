<template>
  <v-container>
    <v-card outlined width="100%">
      <v-container>
        <h2>Choose a Methode</h2>
        <v-radio-group v-model="radioGroup" class="ma-3" hide-details>
          <v-radio :label="`Exact Methode`" :value="0"></v-radio>
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
              v-model="value"
            ></v-select>
          </v-col>
          <v-radio :label="`Heuristic`" :value="1"></v-radio>
          <v-col @click="radioGroup = 1">
            <v-select
              :disabled="radioGroup !== 1"
              :items="items"
              outlined
              placeholder="Instance"
              hide-details
              dense
              item-text="name"
              item-value="value"
              v-model="value"
            ></v-select>
          </v-col>
          <v-radio :label="`Meta-Heuristic`" :value="2"></v-radio>
          <v-col @click="radioGroup = 2">
            <v-select
              :disabled="radioGroup !== 2"
              :items="items"
              outlined
              placeholder="Instance"
              hide-details
              dense
              item-text="name"
              item-value="value"
              v-model="value"
            ></v-select>
          </v-col>
          <v-radio :label="`Hybrid`" :value="3"></v-radio>
          <v-col @click="radioGroup = 3">
            <v-select
              :disabled="radioGroup !== 3"
              :items="items"
              outlined
              placeholder="Instance"
              hide-details
              dense
              item-text="name"
              item-value="value"
              v-model="value"
            ></v-select>
          </v-col>
        </v-radio-group>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import { ipcRenderer, app } from "electron";

export default {
  name: "MethodeSelector",
  props: {
    value: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      items: [
        {
          name: "burma14",
          value: `${
            process.env.NODE_ENV === "development"
              ? "."
              : app.getAppPath("userData")
          }/Python/burma14.tsp`
        },
        {
          name: "bays29",
          value: `${
            process.env.NODE_ENV === "development"
              ? "."
              : app.getAppPath("userData")
          }/Python/bays29.tsp`
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
      this.value = arg;
    });
  }
};
</script>

<style lang="sass" scoped>
</style>