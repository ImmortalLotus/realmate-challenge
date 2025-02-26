
export interface Message {
    id: string;             // Unique identifier for the message
    direction: 'RECEIVED' | 'SENT';  // Direction of the message
    content: string;        // Content of the message
    conversation: string;   // The conversation ID this message belongs to
    timestamp: string;      // The timestamp of the message
  }

