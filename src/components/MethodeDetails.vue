<template>
  <v-container class="py-0">
    <v-card outlined width="100%">
      <v-container class="pt-1">
        <h2 class="mb-3 primary--text">Methode Details</h2>
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
          class="mb-3 primary--text"
          v-if="method.paramters && Object.keys(method.paramters).length > 0"
        >Parameters</h3>
        <div class="gridContainer mt-2" v-if="method.paramters">
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
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "MethodeDetails",
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
  watch: {
    value(newValue) {
      const methods = [
        { Name: "Branch And Bound", paramters: {} },
        { Name: "Exhaustive Search", paramters: {} },
        { Name: "Nearest Neighbour", paramters: {} },
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
            Steps: 100
          }
        },
        { Name: "Genetic Algorithm", paramters: {} },
        { Name: "Genetic Algorithm + 2-OPT", paramters: {} },
        { Name: "Ant Colony + 2-OPT", paramters: {} }
      ];
      let method;
      if (newValue) {
        method = methods.find(element => element.Name === newValue);
      }
      this.method = method ? method : { Name: "", Description: "" };
      if (method && method.Name === "Ant Colony") this.method.paramters.Mode[0];
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