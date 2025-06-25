// src/app/results/page.jsx
"use client";

import { useSearchParams, useRouter } from "next/navigation";
import { useMemo, useEffect, useState } from "react";
import Image from "next/image";
import { RELATIONSHIP_DIMENSIONS } from "../../config/relationshipDimensions";
import { PLAYER_TYPES } from "../../config/playerTypes";

export default function ResultsPage() {
  const params = useSearchParams();
  const router = useRouter();
  const dataParam = params.get("data");
  const [isVisible, setIsVisible] = useState(false);

  // Trigger animations on mount
  useEffect(() => {
    const timer = setTimeout(() => setIsVisible(true), 100);
    return () => clearTimeout(timer);
  }, []);

  // 1) Parse payload
  const result = useMemo(() => {
    if (!dataParam) return null;
    try {
      return JSON.parse(decodeURIComponent(dataParam));
    } catch {
      return null;
    }
  }, [dataParam]);

  if (!result) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-blue-50/30 flex items-center justify-center">
        <div className="text-center p-8 bg-white/80 backdrop-blur-xl rounded-3xl border border-slate-200/60 shadow-2xl">
          <div className="w-16 h-16 mx-auto mb-4 bg-gradient-to-r from-red-500 to-rose-600 rounded-full flex items-center justify-center">
            <span className="text-2xl text-white">⚠️</span>
          </div>
          <p className="text-lg font-medium text-slate-800">
            No analysis data found
          </p>
          <p className="text-sm text-slate-600 mt-2">
            Please return to the analyzer and try again.
          </p>
        </div>
      </div>
    );
  }

  const {
    trait_scores: traitScores,
    conversation_analysis: analysisText,
    conversation_tips: tips,
    player_type: playerKey,
    player_type_summary: ptSummary,
  } = result;

  // 2) Compute each dimension's average (0–10)
  const dims = useMemo(() => {
    const normalize = s =>
      s.trim().toLowerCase().replace(/[_\s]+/g, "");
    const lookup = Object.fromEntries(
      Object.entries(traitScores).map(([k, v]) => [normalize(k), v])
    );

    return Object.entries(RELATIONSHIP_DIMENSIONS).map(([key, dim]) => {
      const vals = dim.traits.map(t => lookup[normalize(t)] ?? 5);
      const avg = vals.reduce((a, b) => a + b, 0) / vals.length;
      return {
        key,
        name: dim.name,
        icon: dim.icon,
        color: dim.color,
        average: avg,
      };
    });
  }, [traitScores]);

  // 3) Persona
  const player = PLAYER_TYPES[playerKey] || PLAYER_TYPES.no_red_flags;
  const imgSrc = `/assets/${playerKey}.png`;

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-blue-50/30 relative overflow-hidden">
      {/* Animated background elements */}
      <div className="absolute inset-0 opacity-20">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-100/40 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-indigo-100/40 rounded-full blur-3xl animate-pulse" style={{animationDelay: '1s'}}></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-72 h-72 bg-purple-100/40 rounded-full blur-3xl animate-pulse" style={{animationDelay: '2s'}}></div>
      </div>

      <div className="relative z-10 max-w-4xl mx-auto p-6 space-y-16">
        {/* Header Section */}
        <section className={`text-center space-y-4 transition-all duration-1000 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 mb-4 shadow-2xl shadow-blue-500/20">
            <span className="text-2xl">📊</span>
          </div>
          <h1 className="text-4xl font-bold tracking-tight bg-gradient-to-r from-slate-800 via-blue-800 to-indigo-800 bg-clip-text text-transparent">
            Analysis Complete
          </h1>
          <div className="max-w-3xl mx-auto p-6 bg-white/60 backdrop-blur-xl rounded-2xl border border-slate-200/60 shadow-lg">
            <p className="text-lg leading-relaxed text-slate-700">
              {analysisText}
            </p>
          </div>
        </section>

        {/* Context transition */}
        <div className={`text-center transition-all duration-1000 delay-300 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
          <div className="inline-flex items-center space-x-3 px-4 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-full border border-blue-200">
            <span className="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></span>
            <p className="text-sm text-slate-600 font-medium italic">
              Based on this analysis, your counterpart most aligns with:
            </p>
            <span className="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></span>
          </div>
        </div>

        {/* Player Persona - Hero Section */}
        <section className={`transition-all duration-1000 delay-500 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
          <div className="relative">
            {/* Background card with glassmorphism */}
            <div className="absolute inset-0 bg-gradient-to-br from-white/80 to-blue-50/80 backdrop-blur-2xl rounded-3xl border border-white/50 shadow-xl"></div>
            
            {/* Content */}
            <div className="relative p-8 flex flex-col items-center space-y-6">
              {/* Image container with floating animation */}
              <div className="relative group">
                <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-full blur-xl opacity-30 group-hover:opacity-50 transition-opacity duration-500"></div>
                <div className="relative w-36 h-36 shadow-xl rounded-full overflow-hidden bg-white border-4 border-white/80 hover:scale-105 transition-transform duration-500">
                  <Image 
                    src={imgSrc} 
                    alt={player.name} 
                    width={144} 
                    height={144}
                    className="object-cover"
                  />
                </div>
                {/* Floating ring animation */}
                <div className="absolute inset-0 rounded-full border-2 border-blue-300/50 animate-ping"></div>
              </div>

              {/* Player name with gradient */}
              <div className="text-center space-y-3">
                <h2 className="text-3xl font-bold bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
                  {player.name}
                </h2>
                {ptSummary && (
                  <div className="max-w-2xl mx-auto p-4 bg-white/50 backdrop-blur-sm rounded-xl border border-white/60">
                    <p className="text-base text-slate-700 leading-relaxed">
                      {ptSummary}
                    </p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </section>

        {/* Relationship Dimensions */}
        <section className={`space-y-6 transition-all duration-1000 delay-700 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
          <div className="text-center">
            <h3 className="text-2xl font-bold text-slate-800 mb-2">
              Relationship Dimensions
            </h3>
            <p className="text-sm text-slate-600 max-w-2xl mx-auto">
              How your conversations score across key relationship areas
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {dims.map(({ key, name, icon, color, average }, index) => (
              <div
                key={key}
                className="group bg-white/70 backdrop-blur-xl border border-slate-200/60 rounded-xl p-5 shadow-lg hover:shadow-xl transition-all duration-500 hover:-translate-y-1"
                style={{
                  animationDelay: `${800 + index * 100}ms`
                }}
              >
                <div className="flex items-center mb-3">
                  <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-100 to-indigo-100 flex items-center justify-center mr-3 group-hover:scale-110 transition-transform duration-300">
                    <span className="text-lg" role="img" aria-label={name}>
                      {icon}
                    </span>
                  </div>
                  <h4 className="text-lg font-semibold text-slate-800">{name}</h4>
                </div>
                
                {/* Animated progress bar */}
                <div className="mb-3">
                  <div className="h-2 bg-slate-200 rounded-full overflow-hidden">
                    <div
                      className="h-full rounded-full transition-all duration-1000 ease-out relative overflow-hidden"
                      style={{
                        width: `${(average / 10) * 100}%`,
                        backgroundColor: color,
                        animationDelay: `${1000 + index * 150}ms`
                      }}
                    >
                      {/* Shimmer effect */}
                      <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent -translate-x-full animate-shimmer"></div>
                    </div>
                  </div>
                </div>
                
                <div className="flex justify-between items-center">
                  <span className="text-xs text-slate-600">Score</span>
                  <div className="flex items-center space-x-1">
                    <span className="text-xl font-bold text-slate-800">
                      {average.toFixed(1)}
                    </span>
                    <span className="text-xs text-slate-500">/ 10</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Tips Section */}
        <section className={`space-y-6 transition-all duration-1000 delay-1000 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
          <div className="text-center">
            <h3 className="text-2xl font-bold text-slate-800 mb-2">
              Tips for Healthy Communication
            </h3>
            <p className="text-sm text-slate-600 max-w-2xl mx-auto">
              Personalized strategies to improve your relationship dynamics
            </p>
          </div>
          
          <div className="grid gap-4">
            {tips.map((tip, index) => (
              <div
                key={index}
                className="group bg-gradient-to-r from-green-50 to-emerald-50 border border-green-200 rounded-xl p-4 hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
                style={{
                  animationDelay: `${1200 + index * 100}ms`
                }}
              >
                <div className="flex items-start space-x-3">
                  <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-green-500 to-emerald-600 rounded-full flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
                    <span className="text-white font-bold text-xs">{index + 1}</span>
                  </div>
                  <p className="text-slate-700 leading-relaxed flex-1">
                    {tip}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Action Section */}
        <section className={`text-center py-8 transition-all duration-1000 delay-1200 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
          <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-2xl p-6 border border-blue-200">
            <h3 className="text-xl font-bold text-slate-800 mb-3">
              Want to analyze another conversation?
            </h3>
            <p className="text-sm text-slate-600 mb-4 max-w-md mx-auto">
              Continue building healthier relationships with more insights
            </p>
            <button 
              onClick={() => router.push('/')}
              className="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl hover:scale-105 transition-all duration-300"
            >
              Analyze Another Conversation
            </button>
          </div>
        </section>
      </div>

      <style jsx>{`
        @keyframes shimmer {
          0% { transform: translateX(-100%); }
          100% { transform: translateX(100%); }
        }
        
        .animate-shimmer {
          animation: shimmer 2s infinite;
        }
        
        @keyframes float {
          0%, 100% { transform: translateY(0px); }
          50% { transform: translateY(-10px); }
        }
        
        .animate-float {
          animation: float 3s ease-in-out infinite;
        }
      `}</style>
    </div>
  );
}