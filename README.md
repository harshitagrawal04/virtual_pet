
# 🧠 3D AI Desktop App – Project Plan

---

## 1. 🎯 Project Overview

**Project Name:**  noirvayl
**Short Description:**  
_A desktop app featuring a 3D character controlled by AI._

**Target Platforms:**  
- [x] Windows  
- [x] macOS  
- [x] Linux  

**Purpose / Vision:**  
_What’s the goal or core purpose of the app?_  

---

## 2. 📦 Features & Scope

### ✅ Core Features
- [ ] 3D character rendering
- [ ] AI-driven character control (dialogue/movement/response)
- [ ] Emotions/expression system
- [ ] Desktop app with cross-platform support
- [ ] Exporting to Windows/Linux/macOS

### 🌱 Optional / Future Features
- [ ] Voice input/output
- [ ] Custom animation editor
- [ ] Background environments
- [ ] eating animation
- [ ] sleeping (ideal) animation

### 🚫 Non-Goals
- [ ] Mobile or web version  
- [ ] Multiplayer functionality  

---

## 3. 🛠️ Technical Stack

**Game Engine:**  
- Godot 4.x 

**Programming Languages:**  
- Python / C++

**AI/ML Stack:**  
- Local model

**3D Tools:**  
- Blender, Mixamo

**Audio Tools:**  
- not decided yet

---

## 4. 🧱 Architecture Plan

**Overview:**
- Engine renders 3D character
- AI module sends control signals
- UI updates with state/output

**Architecture Diagram:**

```plaintext
+------------+       +--------------+      +----------------+
|  AI Logic  | <-->  |  Game Engine | <--> | 3D Assets / UI |
+------------+       +--------------+      +----------------+

```
---

## 5. 🗺️ Roadmap & Milestones

### 🟢 Phase 1: Setup
- [ ] Choose game engine and set up project
- [ ] Install required tools (e.g., Blender, Git, Python)
- [ ] Configure cross-platform build settings
- [ ] Create and test a basic export for all platforms

### 🔵 Phase 2: 3D Prototype
- [ ] Import and display 3D character
- [ ] Add idle animation
- [ ] Implement basic camera and scene controls
- [ ] Create placeholder UI

### 🟣 Phase 3: AI Integration
- [x] Decide AI method (LLM API / **local model** / rules)
- [ ] Set up communication between AI and game engine
- [ ] Use AI to trigger basic character behavior (e.g., animation, text response)
- [ ] Implement basic context memory or dialogue flow

### 🟡 Phase 4: Interaction Layer
- [ ] Add simple chat input/output system
- [ ] Add sound/voice support (TTS or voice lines)
- [ ] Animate based on emotions or dialogue type
- [ ] Improve character responsiveness

### 🟠 Phase 5: Polish & Export
- [ ] Improve UI and add visual feedback
- [ ] Package for Windows, Linux, and macOS
- [ ] Perform usability tests
- [ ] Create installable builds for sharing

---

## 6. 📅 Timeline

| Phase        | Start Date | End Date   | Notes                   |
|--------------|------------|------------|--------------------------|
| Phase 1: Setup          | YYYY-MM-DD | YYYY-MM-DD | Initial tools, repo, builds     |
| Phase 2: 3D Prototype   | YYYY-MM-DD | YYYY-MM-DD | Base character setup            |
| Phase 3: AI Integration | YYYY-MM-DD | YYYY-MM-DD | Link AI + create behavior       |
| Phase 4: Interaction    | YYYY-MM-DD | YYYY-MM-DD | Add UX/UI, sound, reactions     |
| Phase 5: Polish & Export| YYYY-MM-DD | YYYY-MM-DD | Final testing + packaging       |

**Weekly Time Commitment:** ~X hours  
**Target v1 Launch:** YYYY-MM-DD

---

## 7. ⚠️ Risks & Challenges

| Risk                                      | Solution / Mitigation                           |
|-------------------------------------------|--------------------------------------------------|
| AI latency too high                       | Use local model or async messaging              |
| Cross-platform bugs (macOS, Linux issues) | Test exports early; isolate platform-dependent code |
| Animation assets are low quality          | Use Mixamo / ready-made rigged characters       |
| Scope creep                               | Stick to MVP goals and document new ideas separately |
| Difficulty integrating AI + engine        | Start with test environment, simplify prototype |

---

## 8. 🏁 Success Criteria

The project is considered **"v1 complete"** when:
- [ ] 3D character is controllable by AI
- [ ] Emotion/mood expression
- [ ] Core features work on Windows, Linux, and macOS
- [ ] Dialogue system or input/output is functional
- [ ] Basic UI/UX is in place
- [ ] No major bugs, smooth performance

Bonus "stretch" goals:
- [ ] Voice interaction
- [ ] Dynamic scene changes

---

## 9. 🗂️ Resources & References

- **Godot Engine Docs:** https://docs.godotengine.org
- **Mixamo (animations):** https://www.mixamo.com
- **Blender (3D modeling):** https://www.blender.org
- **Free 3D Assets:**  
  - https://sketchfab.com  
  - https://kenney.nl/assets  
  - https://quaternius.com

- **Version Control:**  
  - GitHub: https://github.com  
  - Git tutorials: https://www.atlassian.com/git/tutorials

---

