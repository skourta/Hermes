<template>
  <v-container class="py-0">
    <v-card outlined width="100%">
      <v-container>
        <h2 class="mb-1 primary--text">Results</h2>
        <v-text-field
          label="Cost"
          outlined
          dense
          flat
          hide-details
          readonly
          color="primary"
          class="mt-2"
          v-model="cost"
        ></v-text-field>
        <h3 class="mt-2 primary--text">Tour</h3>
        <div class="d-flex align-center">
          <div class="gridContainer my-2 mr-2" v-if="tour.length < 100">
            <div class="d-flex" v-for="item in tour" :key="item">
              <div class="dot">{{ item }}</div>→
            </div>
          </div>
          <v-spacer></v-spacer>
          <v-btn
            :disabled="!instance || Object.keys(method).length === 0"
            :loading="solving"
            color="primary"
            @click="launch"
          >Launch</v-btn>
        </div>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import { app } from "electron";
import { PythonShell } from "python-shell";
export default {
  name: "Results",
  props: {
    instance: {
      type: String,
      required: true
    },
    method: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      cost: null,
      tour: [],
      solving: false
    };
  },
  computed: {
    fileName() {
      switch (this.method.Name) {
        case "Branch And Bound":
          return "BranchNBound";

        default:
          return "s";
      }
    }
  },
  methods: {
    async launch() {
      this.solving = true;
      await PythonShell.run(
        `${
          process.env.NODE_ENV === "development"
            ? "."
            : app.getAppPath("userData")
        }/Python/${this.fileName}.py`,
        {
          args: [this.instance]
        },
        this.hadnleResults
      );
      // console.log(cost);
    },
    hadnleResults(err, res) {
      if (err) throw err;
      let tour = res[0].substring(1, res[0].length - 1).split(/\s+/);
      if (!tour[0]) tour.shift();
      this.solving = false;
      this.tour = tour;
      this.cost = parseFloat(res[1]);
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