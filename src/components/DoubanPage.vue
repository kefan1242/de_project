<template>
  <div class="page">
    <div class="image-gallery">
      <img :src="d1" alt="Image 1" />
      <img :src="d2" alt="Image 2" />
      <img :src="d3" alt="Image 3" />
      <img :src="d4" alt="Image 4" />
    </div>
    <div class="chat-container">
      <h2>Chat Box</h2>
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
    <!-- 固定在左下角的返回按钮 -->
    <button class="back-button" @click="goBack">返回主界面</button>
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
        { text: "hello", sender: "bot" },
      ],
    };
  },
  methods: {
    goBack() {
      // 路由跳转到主界面
      this.$router.push("/");
    },
    async sendMessage() {
      if (this.userInput.trim() !== "") {
        this.messages.push({ text: this.userInput, sender: "user" });
        const question = this.userInput;
        this.userInput = "";

        setTimeout(() => {
          const botReply = `你说的是：“${question}”，谢谢你的反馈！`;
          this.messages.push({ text: botReply, sender: "bot" });
        }, 1000);

        try {
          const response = await fetch("http://127.0.0.1:8000/gpt/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ question }),
          });

          if (!response.ok) {
            throw new Error("网络响应错误");
          }

          const data = await response.json();
          if (data.success) {
            this.messages.push({
              text: data.data,
              sender: "bot",
            });
          } else {
            this.messages.push({
              text: "后端返回错误，请稍后再试。",
              sender: "bot",
            });
          }
        } catch (error) {
          this.messages.push({
            text: "无法连接到后端服务，请检查网络或后端状态。",
            sender: "bot",
          });
        }
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
  height: 100vh;
  padding: 20px;
  background: linear-gradient(to right, #f9f9f9, #e3f2fd);
  position: relative; /* 需要相对定位以放置固定的按钮 */
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
  background: linear-gradient(to bottom, #ffffff, #e0f7fa);
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

/* 固定左下角的返回按钮样式 */
.back-button {
  position: fixed;
  bottom: 20px;
  left: 20px;
  padding: 10px 20px;
  font-size: 14px;
  background-color: #ff7043;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.back-button:hover {
  background-color: #d84315;
  transform: translateY(-2px);
}
</style>
