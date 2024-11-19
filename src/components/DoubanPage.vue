<template>
  <div class="page">
    <div class="image-gallery">
      <img :src="d1" alt="图片1" />
      <img :src="d2" alt="图片2" />
      <img :src="d3" alt="图片3" />
      <img :src="d4" alt="图片4" />
    </div>
    <div class="chat-container">
      <h2>聊天框</h2>
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
          placeholder="请输入消息..."
          @keyup.enter="sendMessage"
        />
        <button @click="sendMessage">发送</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DoubanPage",
  data() {
    return {
      d1: require("@/assets/d1.png"),
      d2: require("@/assets/d2.png"),
      d3: require("@/assets/d3.png"),
      d4: require("@/assets/d4.png"),
      userInput: "",
      messages: [
        { text: "你好！我是聊天机器人，有什么可以帮你的吗？", sender: "bot" },
      ],
    };
  },
  methods: {
    sendMessage() {
      if (this.userInput.trim() !== "") {
        this.messages.push({ text: this.userInput, sender: "user" });
        const userMessage = this.userInput;
        this.userInput = "";

        setTimeout(() => {
          const botReply = `你说的是：“${userMessage}”，谢谢你的反馈！`;
          this.messages.push({ text: botReply, sender: "bot" });
        }, 1000);
      }
    },
  },
};
</script>

<style>
.page {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  height: 100vh; /* 全屏高度 */
  padding: 20px;
  background: linear-gradient(to right, #f9f9f9, #e3f2fd); /* 增加背景渐变 */
}

.image-gallery {
  display: grid;
  grid-template-columns: 1fr 1fr; /* 两列布局 */
  gap: 20px; /* 图片间距 */
  width: 50%; /* 左侧图片容器宽度调整 */
}

.image-gallery img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease; /* 增加悬停效果 */
}

.image-gallery img:hover {
  transform: scale(1.05); /* 鼠标悬停放大 */
}

.chat-container {
  width: 45%; /* 聊天框宽度 */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  border-radius: 12px;
  background: linear-gradient(to bottom, #ffffff, #e0f7fa); /* 渐变背景 */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.chat-container h2 {
  font-size: 24px;
  margin-bottom: 10px;
  text-align: center;
  color: #00796b;
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
  background-color: #bbdefb;
  text-align: right;
  color: #0d47a1;
}

.message.bot {
  background-color: #c8e6c9;
  text-align: left;
  color: #1b5e20;
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
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #2e8c72;
  transform: translateY(-2px);
}
</style>
