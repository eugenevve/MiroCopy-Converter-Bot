# 🚀 Deployment Guide

This guide describes how to deploy MiroCopy-Converter-Bot to a Linux server using Docker and GitHub.

---

## 📌 1. Server Setup

### Create SSH key for deployment

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_converterbot -C "converterbot-deploy"
```

---

### Add key to authorized keys

```bash
cat ~/.ssh/id_converterbot.pub >> ~/.ssh/authorized_keys
```

---

### View public key

If you need to copy the key manually (for GitHub Deploy Keys):

```bash
cat ~/.ssh/id_converterbot.pub
```

Copy **entire output** and paste into GitHub Deploy Keys.

---

### View private key

If you need to add it to GitHub Secrets (CI/CD):

```bash
cat ~/.ssh/id_converterbot
```

Copy **entire output including BEGIN/END lines** and store it in:

```
GitHub → Settings → Secrets and variables → Actions → SSH_PRIVATE_KEY
```

---

### Important clarification

- `.pub` → public key (safe, goes to GitHub Deploy Keys)
- no extension file → private key (SECRET, goes to GitHub Secrets)

---

### Configure GitHub Deploy Key

On GitHub:

- Go to **Settings → Deploy keys**
- Add new key:

```
Title: Server-Deploy-Key-MiroCopy-Converter-Bot
Key: contents of id_converterbot.pub (use command above to copy)
```

---

### Add GitHub Secrets (for CI/CD)

In **Settings → Secrets and variables → Actions**:

| Name            | Value                             |
| --------------- | --------------------------------- |
| SSH_PRIVATE_KEY | content of ~/.ssh/id_converterbot |
| SERVER_USER     | your server username              |
| SERVER_IP       | your server IP address            |

---

## ⚙️ 2. SSH Config

On the server:

```bash
nano ~/.ssh/config
```

Add:

```bash
Host github-converterbot
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_converterbot
```

---

### Test connection

```bash
ssh -T github-converterbot
```

Expected output:

```
Hi MiroCopy/MiroCopy-ConverterBot! You've successfully authenticated.
```

---

## 📦 3. Clone Project

```bash
git clone git@github-converterbot:eugeneviktorov/MiroCopy-Converter-Bot.git
cd MiroCopy-Converter-Bot
```

---

## 🚀 4. Run Project

```bash
chmod +x deploy.sh
./deploy.sh
```

---

## ⚡ 5. CI/CD (GitHub Actions)

You can manually trigger deployment from GitHub Actions.

Make sure server is running correctly before enabling auto-deploy.

---

## 🧹 6. deploy.sh

If the deploy.sh file has been updated, a manual update may be required.

---

## 📌 Notes

- Ensure `.env` file exists on server
- Never commit secrets to repository
- Use Docker for consistent deployment
