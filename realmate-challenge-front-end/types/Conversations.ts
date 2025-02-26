export type ConversationStatus = "OPEN" | "CLOSED";
import { Message } from "./Messages";

export interface Conversation {
  id: string;
  status: ConversationStatus;
  open_date: string; 
  close_date?: string | null; 
  messages: Message[]; 
}
