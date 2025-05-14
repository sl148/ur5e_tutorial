# UR5e Tutorial (Ubuntu 24.04)

This guide walks you through the steps to connect and control a UR5e robot from your Ubuntu 24.04 laptop.
Useful link: https://sdurobotics.gitlab.io/ur_rtde/examples/examples.html
---

## 1. Robot Network Setup (UR5e Teach Pendant)

On the UR5e teach pendant, navigate to:

Settings → System → Network

Then configure the network as follows:

- **Connection Type**: Static Address  
- **IP Address**: 192.168.1.9  
- **Netmask**: 255.255.255.0  
- **Gateway**: 0.0.0.0

---

## 2. Laptop Network Setup

On your laptop:

1. Open **Network Settings** → **Wired**
2. Under the **IPv4** tab, set the method to **Manual**
3. Add the following:

- **IP Address**: 192.168.1.5  
- **Netmask**: 255.255.255.0  
- **Gateway**: 0.0.0.0

---

## 3. Check Connection

In a terminal, run:

```bash
ping 192.168.1.9
```

If successful, you’ll see sequential packet responses from the robot.

---

## 4. Enable Remote Control on the Robot

On the upper right of the UR5e teach pendant:

- Tap **Local**
- Change it to **Remote**

This enables control from the laptop.

---

## 5. Run Your Code

You are now ready to run your robot control code from your laptop.

---

## 🔧 Troubleshooting

**Issue:**  
You see errors such as:

```
RTDEControlInterface: Could not receive data from robot...
RTDEControlInterface Exception: available: Bad file descriptor
Reconnecting...
RTDEControlInterface: Robot is disconnected, reconnecting...
```

**Solution:**

1. On the UR5e tablet, switch back to **Local** mode
2. Then switch again to **Remote** mode

This will reset the remote control connection.