import type { Conversation } from "@/types/Conversations";
import Link from 'next/link';

export default async function Home() {
  const data = await fetch("http://localhost:8000/conversations/");
  const conversations: Conversation[] = await data.json();

  return (
    <div className="flex justify-center items-center min-h-screen">
    <div className="w-1/2 p-6 border-2 border-gray-300 rounded shadow-lg">
    <ul role="list" className="divide-y divide-gray-100">
      {conversations.map((conversation:Conversation) => (
        <li key={conversation.id} className="flex justify-between gap-x-6 py-5">
          <div className="flex min-w-0 gap-x-4">
            <div className="min-w-0 flex-auto">
            <Link href={`/conversation/${conversation.id}`} className="text-sm font-semibold text-gray-900 hover:text-blue-500">
                {conversation.id}
            </Link>
            </div>
          </div>
          <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
            <p className="text-sm/6 text-gray-900">{conversation.open_date}</p>
            {conversation.close_date ? (
              <div className="mt-1 flex items-center gap-x-1.5">
              <div className="flex-none rounded-full bg-red-500/20 p-1">
                <div className="size-1.5 rounded-full bg-red-500" />
              </div>
              <p className="mt-1 text-xs/5 text-gray-500">
                Conversa fechada as {conversation.close_date}
              </p>
            </div>

            ) : (
              <div className="mt-1 flex items-center gap-x-1.5">
                <div className="flex-none rounded-full bg-emerald-500/20 p-1">
                  <div className="size-1.5 rounded-full bg-emerald-500" />
                </div>
                <p className="text-xs/5 text-gray-500">Conversa aberta às {conversation.open_date}</p>
              </div>
            )}
          </div>
        </li>
      ))}
    </ul>
    </div>
  </div>

    
  );
}
