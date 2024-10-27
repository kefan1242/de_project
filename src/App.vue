<template>
  <div id="app">
    <h1>Chat Interface</h1>
    <div class="chat-container">
      <div class="chat-box">
        <div
          v-for="(message, index) in chatMessages"
          :key="index"
          :class="['message', message.sender === 'User' ? 'user-message' : 'bot-message']"
        >
          <div class="message-content">
            <strong>{{ message.sender }}:</strong> {{ message.text }}
          </div>
        </div>
      </div>
      <div class="input-container">
        <input
          type="text"
          v-model="userInput"
          placeholder="Type your message..."
          @keyup.enter="sendMessage"
        />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: "",
      chatMessages: [],
    };
  },
  methods: {
    sendMessage() {
      if (this.userInput.trim() === "") return;

      // 添加用户消息
      this.chatMessages.push({ sender: "User", text: this.userInput });

      // 模拟 Bot 回复
      setTimeout(() => {
        const botReply = this.getBotReply(this.userInput);
        this.chatMessages.push({ sender: "Bot", text: botReply });
      }, 1000); // 1秒后回复

      // 清空用户输入
      this.userInput = "";
    },
    getBotReply(userMessage) {
      // 简单的 Bot 回复逻辑
      if (userMessage.toLowerCase().includes("hello")) {
        return "Hi there! How can I assist you today?";
      } else if (userMessage.toLowerCase().includes("bye")) {
        return "Goodbye! Have a great day!";
      } else {
        return "I'm here to help! You can ask me anything.";
      }
    },
  },
};
</script>

<style scoped>
#app {
  width: 400px;
  margin: auto;
  text-align: center;
  font-family: Arial, sans-serif;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}

.chat-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.chat-box {
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #f9f9f9;
}

.message {
  margin: 10px 0;
  padding: 10px;
  border-radius: 10px;
  max-width: 70%;
}

.user-message {
  background-color: #daf7a6;
  align-self: flex-end;
}

.bot-message {
  background-color: #f1f0f0;
  align-self: flex-start;
}

.message-content {
  font-size: 14px;
}

.input-container {
  width: 100%;
  display: flex;
}

input[type="text"] {
  width: 80%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
