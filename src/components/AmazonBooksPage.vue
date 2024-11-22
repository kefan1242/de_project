<template>
  <div class="page">
    <div class="image-gallery">
      <img src="amazon1.png" alt="Amazon Books Image 1" />
      <img src="amazon2.png" alt="Amazon Books Image 2" />
      <img src="amazon3.png" alt="Amazon Books Image 3" />
      <img src="amazon4.png" alt="Amazon Books Image 4" />
    </div>
    <div class="chat-container">
      <h2>Amazon Books Chat Box</h2>
      <div class="messages">
        <div
          v-for="(message, index) in messages"
          :key="index"
          :class="['message', message.sender]"
        >
          <p>{{ message.text }}</p>
        </div>
      </div>
      <div class="input-box">
        <input
          type="text"
          v-model="userInput"
          placeholder="Enter your message..."
          @keyup.enter="sendMessage"
        />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
    <!-- Link above the return button -->
    <a href="https://github.com/kefan1242/de_project/tree/main/book_dataset" target="_blank" class="link">View More Information</a>
    <!-- Fixed bottom left return button -->
    <button class="back-button" @click="goBack">Return to Main Page</button>
  </div>
</template>

<script>
export default {
  name: "AmazonBooksPage",
  data() {
    return {
      userInput: "",
      messages: [
        { text: "Welcome to the Amazon Books page, how can I assist you?", sender: "bot" },
      ],
    };
  },
  methods: {
    goBack() {
      this.$router.push("/");
    },
    async sendMessage() {
      if (this.userInput.trim() !== "") {
        this.messages.push({ text: this.userInput, sender: "user" });
        const question = this.userInput;
        this.userInput = "";

        try {
          const response = await fetch("http://127.0.0.1:8000/gpt/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ question }),
          });

          if (!response.ok) {
            throw new Error("Network response error");
          }

          const data = await response.json();
          if (data.success) {
            this.messages.push({
              text: data.data,
              sender: "bot",
            });
          } else {
            this.messages.push({
              text: "Backend returned an error, please try again later.",
              sender: "bot",
            });
          }
        } catch (error) {
          this.messages.push({
            text: "Unable to connect to the backend service, please check your network or backend status.",
            sender: "bot",
          });
        }
      }
    },
  },
};
</script>

<style>
/* Page layout styles */
.page {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  height: 100vh;
  padding: 20px;
  background: linear-gradient(to right, #f3e5f5, #ede7f6);
  position: relative;
}

.image-gallery {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: 50%;
}

.image-gallery img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.image-gallery img:hover {
  transform: scale(1.05);
}

.chat-container {
  width: 45%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  border-radius: 12px;
  background: linear-gradient(to bottom, #ffffff, #f8bbd0);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.chat-container h2 {
  font-size: 24px;
  margin-bottom: 10px;
  text-align: center;
  color: #6a1b9a;
}

.messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 15px;
  padding: 15px;
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
}

.message {
  margin: 10px 0;
  padding: 12px;
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.5;
}

.message.user {
  background-color: #ce93d8;
  text-align: right;
  color: #6a1b9a;
}

.message.bot {
  background-color: #e1bee7;
  text-align: left;
  color: #8e24aa;
}

.input-box {
  display: flex;
  gap: 10px;
  align-items: center;
}

input[type="text"] {
  flex: 1;
  padding: 12px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

button {
  padding: 12px 20px;
  font-size: 14px;
  font-weight: bold;
  background-color: #6a1b9a;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #8e24aa;
  transform: translateY(-2px);
}

/* Fixed bottom left return button */
.back-button {
  position: fixed;
  bottom: 20px;
  left: 20px;
  padding: 10px 20px;
  font-size: 14px;
  background-color: #6a1b9a;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.back-button:hover {
  background-color: #8e24aa;
  transform: translateY(-2px);
}

/* Newly added link styles */
.link {
  position: fixed;
  bottom: 60px;
  left: 20px;
  font-size: 14px;
  color: #6a1b9a;
  text-decoration: underline;
  cursor: pointer;
  transition: color 0.3s ease;
}

.link:hover {
  color: #8e24aa;
}
</style>
