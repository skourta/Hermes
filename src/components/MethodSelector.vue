<template>
  <v-container class="py-0">
    <v-card outlined width="100%">
      <v-container class="pt-1 pb-0">
        <h2 class="primary--text">Choose a Method</h2>
        <v-radio-group v-model="radioGroup" class="ma-3" hide-details>
          <v-radio :label="`Exact Method`" :value="0"></v-radio>
          <v-col @click="radioGroup = 0">
            <v-select
              :disabled="radioGroup !== 0"
              :items="exacts"
              outlined
              placeholder="Method"
              hide-details
              dense
              v-model="method"
            ></v-select>
          </v-col>
          <v-radio :label="`Heuristic`" :value="1"></v-radio>
          <v-col @click="radioGroup = 1">
            <v-select
              :disabled="radioGroup !== 1"
              :items="heuristics"
              outlined
              placeholder="Method"
              hide-details
              dense
              v-model="method"
            ></v-select>
          </v-col>
          <v-radio :label="`Meta-Heuristic`" :value="2"></v-radio>
          <v-col @click="radioGroup = 2">
            <v-select
              :disabled="radioGroup !== 2"
              :items="metas"
              outlined
              dense
              placeholder="Method"
              hide-details
              item-value="value"
              v-model="method"
            ></v-select>
          </v-col>
          <v-radio :label="`Hybrid`" :value="3"></v-radio>
          <v-col @click="radioGroup = 3">
            <v-select
              :disabled="radioGroup !== 3"
              :items="hybrids"
              outlined
              placeholder="Method"
              hide-details
              dense
              item-text="name"
              item-value="value"
              v-model="method"
            ></v-select>
          </v-col>
          <v-radio :label="`Or-Tools by Google`" :value="4"></v-radio>
        </v-radio-group>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "MethodSelector",
  props: {
    value: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      method: "",
      exacts: ["Branch And Bound", "Exhaustive Search"],
      heuristics: ["Nearest Neighbour", "Greedy Algorithm", "2-OPT"],
      metas: ["Ant Colony", "Genetic Algorithm"],
      hybrids: ["Genetic Algorithm + 2-OPT", "Ant Colony + 2-OPT"],
      radioGroup: 0
    };
  },
  watch: {
    method() {
      this.$emit("input", this.method);
    },
    radioGroup(newValue) {
      if (newValue === 4) this.method = "OrTools";
    }
  }
};
</script>

<style lang="sass" scoped>
</style>