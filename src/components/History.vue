<template>
  <div>
    <v-dialog v-model="value" persistent max-width="1000">
      <v-card>
        <v-card-title class="headline primary--text">History of executions</v-card-title>
        <v-data-table
          v-if="history !== null"
          :headers="headers"
          :items="history"
          :items-per-page="5"
          class="elevation-0 mx-3"
        >
          <template v-slot:item.method="{ item }">
            <v-btn small color="primary" outlined @click="displayTour(item)">Details</v-btn>
          </template>
        </v-data-table>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="$emit('input', false)">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="detailsOn" max-width="1000">
      <v-card v-if="selectedEntry !== null">
        <v-card-title class="headline primary--text">Details of Entry</v-card-title>
        <v-col class="gridContainer">
          <div
            v-for="(key,index) in Object.keys(selectedEntry).filter(key => (key !== 'method') && (key !== 'tour') )"
            :key="index"
          >
            <v-text-field
              v-model="selectedEntry[key]"
              outlined
              dense
              flat
              hide-details
              readonly
              color="primary"
              :label="key.toUpperCase()"
            ></v-text-field>
          </div>
          <v-text-field
            v-model="selectedEntry['method'].name"
            outlined
            dense
            flat
            hide-details
            readonly
            color="primary"
            label="METHOD"
          ></v-text-field>
        </v-col>
        <DisplayTour class="mx-3" :tour="selectedEntry.tour"></DisplayTour>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="detailsOn = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import DisplayTour from "./DisplayTour";

export default {
  name: "History",
  components: {
    DisplayTour
  },
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      history: null,
      detailsOn: false,
      selectedEntry: null,
      headers: [
        {
          text: "Instance",
          align: "start",
          value: "instance"
        },
        { text: "Method", value: "method.name" },
        { text: "Cost", value: "cost" },
        // { text: "Tour", value: "tour", width: "100px" },
        { text: "Time(s)", value: "time" },
        { text: "Date", value: "date" },
        { text: "Details", value: "method" }
      ]
    };
  },
  mounted() {
    this.history = this.$db.get("results").value();
    // console.log(this.$db.get("results"));
  },
  methods: {
    displayTour(item) {
      this.selectedEntry = item;
      this.detailsOn = true;
    }
  },
  watch: {
    value(newValue) {
      if (newValue) {
        this.history = this.$db.get("results").value();
        this.history = this.history.filter(x => x);
      }
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