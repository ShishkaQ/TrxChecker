<template>
    <div class="wallet-info">
      <div class="header">
        <div class="address-container">
          <span class="address">{{ address }}</span>
          <button @click="copyAddress" class="copy-button">
            <span v-if="!isCopied">📋</span>
            <span v-else class="copied-text">Скопировано!</span>
          </button>
        </div>
        <button @click="$emit('close')" class="close-button">×</button>
      </div>
  
      <ul class="info-list">
        <li class="info-item">
          <span class="label">Баланс:</span>
          <span class="value">{{ balance }} TRX</span>
        </li>
        <li class="info-item">
          <span class="label">Bandwidth:</span>
          <span class="value">{{ bandwidth }}</span>
        </li>
        <li class="info-item">
          <span class="label">Energy:</span>
          <span class="value">{{ energy }}</span>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      address: {
        type: String,
        required: true
      },
      balance: Number,
      bandwidth: Number,
      energy: Number
    },
    data() {
      return {
        isCopied: false
      }
    },
    methods: {
      copyAddress() {
        navigator.clipboard.writeText(this.address)
          .then(() => {
            this.isCopied = true
            setTimeout(() => {
              this.isCopied = false
            }, 2000)
          })
          .catch(() => {
            alert('Не удалось скопировать адрес')
          })
      }
    }
  }
  </script>
  
  <style scoped>
  .wallet-info {
    margin-top: 2rem;
    padding: 1.5rem;
    background: var(--bg-200);
    border-radius: 8px;
    animation: slideUp 0.3s ease;
    position: relative;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1.5rem;
  }
  
  .address-container {
    flex-grow: 1;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    max-width: 90%;
  }
  
  .address {
    font-family: monospace;
    font-size: 0.9rem;
    color: var(--text-200);
    opacity: 0.9;
    word-break: break-all;
  }
  
  .copy-button {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.25rem;
    color: var(--primary-300);
    transition: opacity 0.2s;
    flex-shrink: 0;
  }
  
  .copy-button:hover {
    opacity: 0.8;
  }
  
  .copied-text {
    color: #42b983;
    font-size: 0.8rem;
  }
  
  .close-button {
    background: none;
    border: none;
    font-size: 1.5rem;
    color: var(--text-200);
    cursor: pointer;
    padding: 0 0.5rem;
    opacity: 0.7;
    transition: opacity 0.2s;
  }
  
  .close-button:hover {
    opacity: 1;
  }
  
  .info-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .info-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background: var(--bg-300);
    border-radius: 6px;
  }
  
  .label {
    font-size: 0.9rem;
    color: var(--text-200);
    opacity: 0.8;
  }
  
  .value {
    font-size: 1rem;
    font-weight: 600;
    color: var(--accent-200);
  }
  
  @keyframes slideUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @media (max-width: 480px) {
    .address {
      font-size: 0.8rem;
    }
    
    .info-item {
      padding: 0.75rem;
    }
  }
  </style>