<template>
  <v-dialog v-model="value" persistent max-width="1000">
    <v-card>
      <v-card-title class="headline">History of executions</v-card-title>
      <v-data-table
        v-if="history !== null"
        :headers="headers"
        :items="history"
        :items-per-page="5"
        class="elevation-0"
      ></v-data-table>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="red darken-1" text @click="$emit('input', false)">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
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
      history: null,
      headers: [
        {
          text: "Instance",
          align: "start",
          value: "instance"
        },
        { text: "Method", value: "method.name" },
        { text: "Cost", value: "cost" },
        { text: "Tour", value: "tour", width: "100px" },
        { text: "Time", value: "time" },
        { text: "Date", value: "date" }
      ]
    };
  },
  mounted() {
    this.history = this.$db.get("results").value();
    // console.log(this.$db.get("results"));
  }
};
</script>