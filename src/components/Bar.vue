<template>
  <v-container class="pb-0">
    <v-card outlined width="100%" class="myAppBar primary" dark>
      <v-row class="px-6 align-center">
        <h2>Solving TSP</h2>
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
  </v-container>
</template>

<script>
import History from "./History";
export default {
  name: "Bar",
  components: {
    History
  },
  data() {
    return {
      items: ["History", "About"],
      history: false
    };
  },
  methods: {
    handleClick(title) {
      this[title.toLowerCase()] = true;
    }
  }
};
</script>
