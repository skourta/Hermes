<template>
  <v-container class="pb-0">
    <v-card outlined width="100%">
      <v-container class="pt-1">
        <h2 class="mb-0 primary--text">Results</h2>
        <v-row>
          <v-col cols="6" class="pt-0">
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
          </v-col>
          <v-col cols="6" class="pt-0">
            <v-text-field
              label="Time (s)"
              outlined
              dense
              flat
              hide-details
              readonly
              color="primary"
              class="mt-2"
              v-model="time"
            ></v-text-field>
          </v-col>
        </v-row>

        <DisplayTour :tour="tour"></DisplayTour>
        <div class="d-flex align-center">
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
import DisplayTour from "./DisplayTour";
import { app } from "electron";
import { PythonShell } from "python-shell";
export default {
  name: "Results",
  components: {
    DisplayTour
  },
  props: {
    instance: {
      type: String,
      required: true
    },
    method: {
      type: String,
      required: true
    },
    paramters: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      cost: null,
      tour: [],
      time: null,
      solving: false,
      argss: []
    };
  },
  computed: {
    args() {
      switch (this.method) {
        case "Branch And Bound":
          return { name: "BranchNBound", args: [this.instance] };
        case "Nearest Neighbour":
          return {
            name: "PPV",
            args: [this.instance, `--start=${this.paramters.start}`]
          };
        case "2-OPT":
          return { name: "2OPT", args: [this.instance] };
        case "Greedy Algorithm":
          return {
            name: "Greedy",
            args: [
              this.instance
              // `--start=${this.paramters.start}`
            ]
          };
        case "Exhaustive Search":
          return { name: "BruteForce", args: [this.instance] };
        case "Ant Colony":
          return {
            name: "AC",
            args: [
              `--instance=${this.instance}`,
              `--mode=${this.paramters.selectedMode}`,
              `--colony_size=${this.paramters["Colony Size"]}`,
              `--elitist_weight=${this.paramters["Elisit Weight"]}`,
              `--min_scaling_factor=${this.paramters["Min Scaling Factor"]}`,
              `--alpha=${this.paramters["Alpha"]}`,
              `--beta=${this.paramters["Beta"]}`,
              `--rho=${this.paramters["Rho"]}`,
              `--pheromone_deposit_weight=${this.paramters["Pheromone Deposit Weight"]}`,
              `--initial_pheromone=${this.paramters["Initial Pheromone"]}`,
              `--steps=${this.paramters["Steps"]}`
            ]
          };
        case "Genetic Algorithm":
          return {
            name: "AG",
            args: [
              this.instance,
              `--population_size=${this.paramters.population_size}`,
              `--nbgenerations=${this.paramters["nbgenerations"]}`,
              `--parents_size=${this.paramters["parents_size"]}`,
              `--eliteSize=${this.paramters["eliteSize"]}`,
              `--genAlgo=${this.paramters["genAlgo"]}`,
              `--SelectionAlgo=${this.paramters["SelectionAlgo"]}`,
              `--nbPointCroisement=${this.paramters["nbPointCroisement"]}`,
              `--probaMutation=${this.paramters["probaMutation"]}`,
              `--remplacementAlgo=${this.paramters["remplacementAlgo"]}`
            ]
          };
        case "Tabu Search":
          return {
            name: "Tabu",
            args: [
              this.instance,
              `--iterations=${this.paramters.iterations}`,
              `--size=${this.paramters.size}`,
              `--start=${this.paramters.start}`
            ]
          };

        case "OrTools":
          return { name: "or_tools", args: [this.instance] };
        default:
          return "s";
      }
    }
  },
  methods: {
    async launch() {
      this.solving = true;
      // ipcRenderer.send("test");
      await PythonShell.run(
        `${
          process.env.NODE_ENV === "development"
            ? "."
            : app.getAppPath("userData")
        }/Python/${this.args.name}.py`,
        {
          args: this.args.args
        },
        this.hadnleResults
      );
      // console.log(cost);
    },
    hadnleResults(err, res) {
      if (err) throw err;
      let tour = res[0].substring(1, res[0].length - 1).split(/,?\s+/);
      if (!tour[0]) tour.shift();
      if (!tour[tour.length - 1]) tour.pop();
      this.solving = false;
      this.tour = tour;
      this.cost = parseFloat(res[1]);
      this.time = parseFloat(res[2]);
      // console.log(res);
      let path = this.instance.split("/");
      const instanceName = path[path.length - 1];

      this.$db
        .get("results")
        .push({
          instance: instanceName,
          method: {
            name: this.method,
            parameters: this.paramters
          },
          cost: this.cost,
          tour: this.tour,
          time: this.time,
          date: new Date()
        })
        .write();
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