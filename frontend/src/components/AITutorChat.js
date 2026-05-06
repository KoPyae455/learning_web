import React, { useState, useRef, useEffect } from "react";
import { 
  Box, Fab, Paper, Typography, TextField, IconButton, 
  List, ListItem, ListItemText, Divider, CircularProgress,
  Slide
} from "@mui/material";
import { 
  Chat as ChatIcon, Close as CloseIcon, Send as SendIcon, 
  SmartToy as BotIcon, Person as PersonIcon
} from "@mui/icons-material";
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

const AITutorChat = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { text: "Hello! I am your AI Tutor. How can I help you today?", sender: "bot" }
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isOpen]);

  const toggleChat = () => setIsOpen(!isOpen);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input.trim();
    setMessages(prev => [...prev, { text: userMessage, sender: "user" }]);
    setInput("");
    setIsLoading(true);

    try {
      const response = await axios.post(`${API_URL}/api/ai/chat/`, {
        message: userMessage
      });
      
      setMessages(prev => [...prev, { text: response.data.reply, sender: "bot" }]);
    } catch (error) {
      console.error("AI Chat Error:", error);
      setMessages(prev => [...prev, { text: "Sorry, I am having trouble connecting to the server. Please try again later.", sender: "bot" }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <>
      <Slide direction="up" in={isOpen} mountOnEnter unmountOnExit>
        <Paper
          elevation={6}
          sx={{
            position: "fixed",
            bottom: 90,
            right: 20,
            width: 350,
            height: 500,
            display: "flex",
            flexDirection: "column",
            zIndex: 1000,
            borderRadius: 3,
            overflow: "hidden"
          }}
        >
          {/* Header */}
          <Box sx={{ bgcolor: "primary.main", color: "white", p: 2, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <Box sx={{ display: "flex", alignItems: "center", gap: 1 }}>
              <BotIcon />
              <Typography variant="h6" sx={{ fontSize: "1.1rem" }}>AI Tutor</Typography>
            </Box>
            <IconButton size="small" onClick={toggleChat} sx={{ color: "white" }}>
              <CloseIcon />
            </IconButton>
          </Box>

          {/* Messages */}
          <Box sx={{ flexGrow: 1, p: 2, overflowY: "auto", bgcolor: "#f9f9f9" }}>
            <List>
              {messages.map((msg, index) => (
                <ListItem 
                  key={index} 
                  sx={{ 
                    flexDirection: "column", 
                    alignItems: msg.sender === "user" ? "flex-end" : "flex-start",
                    padding: "4px 0"
                  }}
                >
                  <Paper 
                    elevation={1}
                    sx={{ 
                      p: 1.5, 
                      maxWidth: "85%",
                      bgcolor: msg.sender === "user" ? "primary.main" : "white",
                      color: msg.sender === "user" ? "white" : "text.primary",
                      borderRadius: msg.sender === "user" ? "20px 20px 0px 20px" : "20px 20px 20px 0px"
                    }}
                  >
                    <Typography variant="body2" sx={{ whiteSpace: "pre-wrap" }}>
                      {msg.text}
                    </Typography>
                  </Paper>
                </ListItem>
              ))}
              {isLoading && (
                <ListItem sx={{ justifyContent: "flex-start", padding: "4px 0" }}>
                  <Paper elevation={0} sx={{ p: 1.5, bgcolor: "transparent" }}>
                    <CircularProgress size={20} />
                  </Paper>
                </ListItem>
              )}
              <div ref={messagesEndRef} />
            </List>
          </Box>
          
          <Divider />

          {/* Input Area */}
          <Box sx={{ p: 2, display: "flex", gap: 1, alignItems: "center", bgcolor: "white" }}>
            <TextField
              fullWidth
              size="small"
              placeholder="Ask me anything..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyPress}
              multiline
              maxRows={3}
              sx={{ "& fieldset": { borderRadius: 3 } }}
            />
            <IconButton 
              color="primary" 
              onClick={handleSend}
              disabled={!input.trim() || isLoading}
              sx={{ bgcolor: "primary.light", color: "white", "&:hover": { bgcolor: "primary.main" } }}
            >
              <SendIcon size="small" />
            </IconButton>
          </Box>
        </Paper>
      </Slide>

      <Fab 
        color="primary" 
        aria-label="chat" 
        onClick={toggleChat}
        sx={{
          position: "fixed",
          bottom: 20,
          right: 20,
          zIndex: 1000,
        }}
      >
        {isOpen ? <CloseIcon /> : <ChatIcon />}
      </Fab>
    </>
  );
};

export default AITutorChat;
