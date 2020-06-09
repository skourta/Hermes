<template>
  <v-container style="height: 100%;    max-width: 100%;" class="pt-0">
    <v-row>
      <v-col class="fill-height py-0" cols="4">
        <v-row>
          <InstanceSelector v-model="instance"></InstanceSelector>
        </v-row>
        <v-row>
          <MethodeSelector v-model="method"></MethodeSelector>
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
          <MethodeDetails v-model="method" @setMethod="setMethod"></MethodeDetails>
        </v-row>
        <v-row>
          <Results :method="fullMethod" :instance="instance"></Results>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import { ipcRenderer, app } from "electron";
// import { PythonShell } from "python-shell";

import InstanceSelector from "./InstanceSelector";
import MethodeSelector from "./MethodeSelector";
import InstanceDetails from "./InstanceDetails";
import MethodeDetails from "./MethodeDetails";
import Bar from "./Bar";
import Results from "./Results";
export default {
  name: "MainPage",
  components: {
    InstanceSelector,
    MethodeSelector,
    InstanceDetails,
    MethodeDetails,
    Results,
    Bar
  },

  data: () => ({
    instance: "",
    method: "",
    fullMethod: {}
  }),
  methods: {
    setMethod(arg) {
      this.fullMethod.paramters = arg.paramters;
    }
  },
  watch: {
    instance(newValue) {
      this.fullMethod.Name = newValue;
    }
  }
};
</script>
