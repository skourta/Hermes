<template>
  <div>
    <v-dialog v-model="value" persistent overlay-opacity="0" max-width="1000" class="elevation-0">
      <v-card class="text-center elevation-0">
        <h1 class="primary--text py-4">Hermes</h1>
        <h3 class="primary--text">Description</h3>
        <p style="width: 60%;margin: 1rem auto; text-align: justify">
          <strong>Hermes</strong> is a hybrid desktop application built using Electron and Vue to solve the Symmetric Traveling Salesman Problem(TSP), it provides different methods written in Python to solve TSP varying from exact ones to hybrid meta-heuristics.
        </p>
        <v-container>
          <h3 class="primary--text">Team</h3>
          <div class="gridContainer mt-5">
            <v-row
              align="center"
              class="mx-3"
              no-gutters
              v-for="(user,index) in users"
              :key="index"
            >
              <v-avatar size="60px">
                <v-img v-if="user.img" alt="Avatar" :src="require(`../assets/${user.img}`)" />
                <span v-else>user.name[0]</span>
              </v-avatar>
              <strong class="ml-5 text-display" v-html="user.name"></strong>
            </v-row>
          </div>
        </v-container>
        <h3 class="primary--text">Made with ❤️ and ☕</h3>
        <h3 class="primary--text">{{(new Date()).getFullYear()}}</h3>
        <!--  -->
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="$emit('input', false)">Close</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "History",
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      about: null,
      users: [
        {
          name: "BENABED Youcef",
          img: "youcef.jpg"
        },
        {
          name: "BENBELGACEM Rahma Aya",
          img: "aya.jpg"
        },
        {
          name: "BENDJABALLAH Oussama",
          img: "oussama.jpg"
        },
        {
          name: "IFERROUDJENE Mouloud",
          img: "mouloud.jpg"
        },
        {
          name: "TAHMI Omar",
          img: "omar.jpg"
        },
        {
          name: "KOURTA Smail",
          img: "sk.jpeg"
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.gridContainer {
  width: 80%;
  margin: 0 auto;
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr 1fr;
}
</style>