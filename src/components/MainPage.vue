<template>
  <v-container style="height: 100%;    max-width: 100%;" class="pt-0">
    <v-row>
      <v-col class="fill-height py-0" cols="4">
        <v-row>
          <InstanceSelector v-model="instance"></InstanceSelector>
        </v-row>
        <v-row>
          <MethodSelector v-model="method"></MethodSelector>
        </v-row>
      </v-col>
      <v-col cols="8" class="fill-height py-0">
        <v-row>
          <Bar></Bar>
        </v-row>
        <v-row>
          <InstanceDetails v-model="instance"></InstanceDetails>
        </v-row>
        <v-row>
          <MethodDetails v-model="method" @setMethod="setMethod"></MethodDetails>
        </v-row>
        <v-row>
          <Results :method="method" :instance="instance" :paramters="paramters"></Results>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import { ipcRenderer, app } from "electron";
// import { PythonShell } from "python-shell";

import InstanceSelector from "./InstanceSelector";
import MethodSelector from "./MethodSelector";
import InstanceDetails from "./InstanceDetails";
import MethodDetails from "./MethodDetails";
import Bar from "./Bar";
import Results from "./Results";
export default {
  name: "MainPage",
  components: {
    InstanceSelector,
    MethodSelector,
    InstanceDetails,
    MethodDetails,
    Results,
    Bar
  },

  data: () => ({
    instance: "",
    method: "",
    paramters: {}
  }),
  methods: {
    setMethod(arg) {
      this.paramters = arg.paramters;
    }
  }
};
</script>
