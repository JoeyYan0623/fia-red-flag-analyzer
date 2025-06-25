// src/components/ProgressSpinner.jsx
"use client";

import { useEffect, useState } from "react";

export default function ProgressSpinner({ onComplete }) {
  const [pct, setPct] = useState(0);

  useEffect(() => {
    if (pct >= 100) {
      onComplete();
      return;
    }
    const id = setTimeout(() => setPct(p => p + Math.ceil(Math.random() * 10)), 200);
    return () => clearTimeout(id);
  }, [pct, onComplete]);

  return (
    <div className="flex flex-col items-center space-y-2">
      <div className="w-16 h-16 border-4 border-blue-200 rounded-full border-t-blue-600 animate-spin" />
      <div className="text-lg font-medium">{pct}%</div>
      <div className="text-gray-600 text-sm">Analyzing...</div>
    </div>
  );
}
