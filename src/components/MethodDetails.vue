<template>
  <v-container class="py-0">
    <v-card outlined width="100%">
      <v-container class="pt-1">
        <h2 class="mb-1 primary--text">Method Details</h2>
        <v-text-field
          v-model="method['Name']"
          outlined
          dense
          flat
          hide-details
          readonly
          color="primary"
          label="Name"
        ></v-text-field>
        <h3
          class="mb-0 primary--text"
          v-if="method.paramters && Object.keys(method.paramters).length > 0"
        >Parameters</h3>
        <div v-if="method.paramters">
          <div class="gridContainer mt-2" v-if=" method.Name !== 'Genetic Algorithm'">
            <div v-for="key in Object.keys(method.paramters)" :key="key">
              <v-text-field
                v-if="(key !== 'Mode') && (key !== 'selectedMode')"
                v-model="method.paramters[key]"
                outlined
                dense
                flat
                hide-details
                color="primary"
                :label="key"
              ></v-text-field>
              <div v-else>
                <v-select
                  v-if="key === 'Mode'"
                  :items="method.paramters[key]"
                  outlined
                  placeholder="Mode"
                  hide-details
                  dense
                  v-model="method.paramters.selectedMode"
                ></v-select>
              </div>
            </div>
          </div>
          <div class="gridContainer mt-2" v-else>
            <div v-for="key in parametersAG.nonSelects" :key="key">
              <v-text-field
                v-model="method.paramters[key]"
                outlined
                dense
                flat
                hide-details
                color="primary"
                :label="key"
              ></v-text-field>
            </div>
            <v-select
              v-for="select in parametersAG.selects"
              :key="select"
              :items="method.paramters[select]"
              outlined
              placeholder="Mode"
              hide-details
              dense
              v-model="method.paramters[select.slice(0,-1)]"
              :label="select"
            ></v-select>
          </div>
        </div>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
const methods = [
  { Name: "Branch And Bound", paramters: {} },
  { Name: "Exhaustive Search", paramters: {} },
  {
    Name: "Nearest Neighbour",
    paramters: {
      start: 0
    }
  },
  {
    Name: "2-OPT",
    paramters: {}
  },
  {
    Name: "Greedy Algorithm",
    paramters: {
      // start: 0
    }
  },
  {
    Name: "Ant Colony",
    paramters: {
      Mode: ["ACS", "Elitist", "MinMax"],
      "Colony Size": 10,
      "Elisit Weight": 1,
      "Min Scaling Factor": 0.001,
      Alpha: 1.0,
      Beta: 3.0,
      Rho: 0.1,
      "Pheromone Deposit Weight": 1.0,
      "Initial Pheromone": 1.0,
      Steps: 100,
      selectedMode: "ACS"
    }
  },
  {
    Name: "Ant Colony [2OPT]",
    paramters: {
      Mode: ["ACS", "Elitist", "MinMax"],
      "Colony Size": 10,
      "Elisit Weight": 1,
      "Min Scaling Factor": 0.001,
      Alpha: 1.0,
      Beta: 3.0,
      Rho: 0.1,
      "Pheromone Deposit Weight": 1.0,
      "Initial Pheromone": 1.0,
      Steps: 100,
      selectedMode: "ACS"
    }
  },
  {
    Name: "Ant Colony + 2OPT",
    paramters: {
      Mode: ["ACS", "Elitist", "MinMax"],
      "Colony Size": 10,
      "Elisit Weight": 1,
      "Min Scaling Factor": 0.001,
      Alpha: 1.0,
      Beta: 3.0,
      Rho: 0.1,
      "Pheromone Deposit Weight": 1.0,
      "Initial Pheromone": 1.0,
      Steps: 100,
      selectedMode: "ACS"
    }
  },
  {
    Name: "Genetic Algorithm",
    paramters: {
      population_size: 28,
      nbgenerations: 2,
      parents_size: 14,
      eliteSize: 2,
      genAlgos: ["PPV", "Random"],
      SelectionAlgos: ["Tournoi", "Elitiste", "RouletteWheel"],
      nbPointCroisement: 2,
      probaMutation: "None",
      remplacementAlgos: [
        "Tournoi",
        "Elitiste",
        "RouletteWheel",
        "Generationnel"
      ],
      remplacementAlgo: "Tournoi",
      genAlgo: "PPV",
      SelectionAlgo: "Tournoi"
    }
  },
  {
    Name: "Tabu Search",
    paramters: {
      iterations: 1000,
      size: 20,
      start: 0
    }
  },
  { Name: "Genetic Algorithm + 2-OPT", paramters: {} },
  { Name: "Ant Colony + 2-OPT", paramters: {} },
  {
    Name: "OrTools",
    paramters: {}
  }
];
export default {
  name: "MethodDetails",
  props: {
    value: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      method: {
        Name: ""
      }
    };
  },
  computed: {
    parametersAG() {
      let nonSelects = [];
      let selects = [];
      for (const key in this.method.paramters) {
        if (
          key !== "genAlgos" &&
          key !== "genAlgo" &&
          key !== "remplacementAlgos" &&
          key !== "remplacementAlgo" &&
          key !== "SelectionAlgos" &&
          key !== "SelectionAlgo"
        ) {
          nonSelects.push(key);
        } else {
          if (
            key !== "genAlgo" &&
            key !== "remplacementAlgo" &&
            key !== "SelectionAlgo"
          )
            selects.push(key);
        }
      }
      return { nonSelects: nonSelects, selects: selects };
    }
  },
  watch: {
    value(newValue) {
      let method;
      if (newValue) {
        method = methods.find(element => element.Name === newValue);
      }
      this.method = method ? method : { Name: "", Description: "" };
      this.$emit("setMethod", this.method);
    }
  }
};
</script>

<style lang="scss" scoped>
.gridContainer {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}
</style>