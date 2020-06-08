<template>
  <v-container style="height: 100%;    max-width: 100%;">
    <v-row style="height:100%">
      <v-col cols="4">
        <v-row>
          <InstanceSelector v-model="instance"></InstanceSelector>
        </v-row>
        <v-row>
          <!-- <MethodeSelector></MethodeSelector> -->
        </v-row>
      </v-col>
      <v-col cols="8"></v-col>
    </v-row>
  </v-container>
</template>

<script>
// import { ipcRenderer, app } from "electron";
// import { PythonShell } from "python-shell";

import InstanceSelector from "./InstanceSelector";
// import MethodeSelector from "./MethodeSelector";
export default {
  name: "HelloWorld",
  components: {
    InstanceSelector
    // MethodeSelector
  },

  data: () => ({
    instance: ""
  }),
  methods: {
    testPython() {
      // ipcRenderer.send("readFile", "async ping");
    }
  },
  mounted() {
    // ipcRenderer.on("fileRead", (event, arg) => {
    //   console.log(arg);
    //   PythonShell.run(
    //     `${
    //       process.env.NODE_ENV === "development"
    //         ? "."
    //         : app.getAppPath("userData")
    //     }/Python/BranchNBound.py`,
    //     {
    //       args: [arg]
    //     },
    //     function(err, res) {
    //       if (err) throw err;
    //       console.log("finished");
    //       let tour = res[0].substring(1, res[0].length - 1).split(/\s+/);
    //       if (!tour[0]) tour.shift();
    //       console.log(tour);
    //       console.log(parseFloat(res[1]));
    //     }
    //   );
    // });
  }
};
</script>
