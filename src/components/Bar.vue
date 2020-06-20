<template>
  <v-container class="pb-0">
    <v-card outlined width="100%" class="myAppBar primary" dark>
      <v-row class="px-6 align-center">
        <h2>
          Hermes:
          <span class="text-body-1">Solving TSP</span>
        </h2>
        <v-spacer></v-spacer>
        <h4 class="pr-2">Equipe 13</h4>
        <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon v-bind="attrs" v-on="on">
              <v-icon>mdi-menu</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item v-for="(item, index) in items" :key="index" @click="handleClick(item)">
              <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-row>
    </v-card>
    <History v-model="history"></History>
    <About v-model="about"></About>
  </v-container>
</template>

<script>
import History from "./History";
import About from "./About";
export default {
  name: "Bar",
  components: {
    History,
    About
  },
  data() {
    return {
      items: ["History", "About"],
      history: false,
      about: true
    };
  },
  methods: {
    handleClick(title) {
      this[title.toLowerCase()] = true;
    }
  },
  computed: {
    combined() {
      return this.history || this.about;
    }
  },
  watch: {
    combined(newValue) {
      if (!newValue)
        document
          .getElementsByClassName("v-application--wrap")[0]
          .classList.remove("blur");
      else
        document
          .getElementsByClassName("v-application--wrap")[0]
          .classList.add("blur");
    }
  },
  mounted() {
    document
      .getElementsByClassName("v-application--wrap")[0]
      .classList.add("blur");
  }
};
</script>
<style>
.blur {
  filter: blur(5px);
  transition: filter 0.5s cubic-bezier(0.075, 0.82, 0.165, 1);
}
</style>
