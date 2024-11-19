<template>
    <div class="detail-page">
      <div class="image-container">
        <img :src="imageSrc" :alt="title" />
      </div>
      <div class="chat-container">
        <h2>{{ title }}</h2>
        <p>此区域为智能语言模块的对话框，后续可集成相关功能。</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "DetailPage",
    props: {
      title: {
        type: String,
        required: true,
      },
      imageSrc: {
        type: String,
        required: true,
      },
    },
  };
  </script>
  
  <style>
  .detail-page {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 80vh;
    padding: 20px;
  }
  .image-container img {
    max-width: 40%;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  .chat-container {
    width: 50%;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  .chat-container h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  .chat-container p {
    font-size: 16px;
    color: #666;
  }
  </style>
  