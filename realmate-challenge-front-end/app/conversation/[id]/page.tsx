// app/conversations/[id]/page.tsx

import React from 'react';
import { Conversation } from '@/types/Conversations';
const ConversationPage = async ({ params }: { params: { id: string } }) => {
  // Await params before accessing `id`
  const { id } = await params;

  // Fetch conversation data directly in the server component
  const res = await fetch(`http://localhost:8000/conversations/${id}`);
  const resJson=await res.json()
  console.log(resJson)
  const conversation: Conversation =resJson;
  console.log(conversation)
  if (!conversation) {
    return <div>Conversation not found</div>;
  }

  return (
    <div className="flex justify-center items-center min-h-screen">
    <div className="w-1/2 p-6 border-2 border-gray-300 rounded shadow-lg">
    <h5 className="text-1xl font-extrabold leading-tight text-gray-900">
          Conversation ID: {id}
    </h5>
    {conversation.status==="CLOSED" ? (
              <div className="mt-1 flex items-center gap-x-1.5">
              <div className="flex-none rounded-full bg-red-500/20 p-1">
                <div className="size-1.5 rounded-full bg-red-500" />
              </div>
              <p className="mt-1 text-xs/5 text-gray-500">
                Conversa fechada
              </p>
            </div>

            ) : (
              <div className="mt-1 flex items-center gap-x-1.5">
                <div className="flex-none rounded-full bg-emerald-500/20 p-1">
                  <div className="size-1.5 rounded-full bg-emerald-500" />
                </div>
                <p className="text-xs/5 text-gray-500">Conversa aberta</p>
              </div>
            )}
    <div className="p-4 space-y-4 max-w-3xl mx-auto">
      <div className="flex flex-col space-y-4">
        {conversation.messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${message.direction === 'SENT' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-xs px-4 py-2 rounded-lg ${
                message.direction === 'SENT'
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-200 text-black'
              }`}
            >
              <p>{message.content}</p>
              <span className="text-xs text-gray-500">
                {new Date(message.timestamp).toLocaleTimeString()}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
    </div>
    </div>
  );
};

export default ConversationPage;
