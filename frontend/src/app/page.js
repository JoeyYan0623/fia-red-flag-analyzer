'use client';

import { useRef, useState } from 'react';
import { useRouter } from 'next/navigation';

export default function Home() {
  const fileInputRef = useRef(null);
  const [fileList, setFileList] = useState([]);
  const [relationshipType, setRelationshipType] = useState('');
  const [context, setContext] = useState('');
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleFilesChange = (e) => {
    const files = Array.from(e.target.files);
    setFileList(files);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!fileList.length || !relationshipType || !context) return;

    setLoading(true);
    const formData = new FormData();
    fileList.forEach((file) => formData.append('files', file));
    formData.append('relationship_type', relationshipType);
    formData.append('context', context);

    try {
      const res = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) throw new Error('Analysis failed');

      const json = await res.json();
      const encoded = encodeURIComponent(JSON.stringify(json));
      router.push(`/results?data=${encoded}`);
    } catch (err) {
      alert('Error analyzing conversation. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-blue-50/30 flex flex-col items-center justify-center px-4 py-8 relative overflow-hidden">
      {/* Subtle background elements */}
      <div className="absolute inset-0 opacity-30">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-100/40 rounded-full blur-3xl"></div>
        <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-indigo-100/40 rounded-full blur-3xl"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-72 h-72 bg-purple-100/40 rounded-full blur-3xl"></div>
      </div>

      {/* Main content */}
      <div className="relative z-10 max-w-lg w-full mx-auto">
        {/* Header */}
        <div className="text-center mb-6">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 mb-4 shadow-xl shadow-blue-500/20">
            <span className="text-2xl">🔍</span>
          </div>
          <h1 className="text-3xl font-bold tracking-tight mb-2 text-slate-800">
            <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              FIA Red Flag Analyzer
            </span>
          </h1>
          <p className="text-base text-slate-600 font-medium max-w-sm mx-auto">
            Detect hidden power tactics in your conversations.
          </p>
        </div>

        {/* Form Card */}
        <div className="bg-white/80 backdrop-blur-xl rounded-3xl border border-slate-200/60 p-6 shadow-xl shadow-slate-200/50">
          <form onSubmit={handleSubmit} className="space-y-4">
            {/* Upload Section */}
            <div>
              <label className="block text-sm font-semibold mb-2 text-slate-800">
                Upload Files <span className="text-xs text-slate-500 font-normal">(txt, pdf, image)</span>
              </label>
              <div
                className="group relative border-2 border-dashed border-slate-300 rounded-xl p-4 bg-slate-50/50 hover:bg-blue-50/50 hover:border-blue-300 transition-all duration-300 cursor-pointer"
                onClick={() => fileInputRef.current?.click()}
              >
                <input
                  ref={fileInputRef}
                  type="file"
                  multiple
                  hidden
                  accept=".txt,.pdf,image/*"
                  onChange={handleFilesChange}
                />
                <div className="text-center">
                  <div className="w-10 h-10 mx-auto mb-2 rounded-xl bg-gradient-to-br from-blue-100 to-indigo-100 flex items-center justify-center group-hover:scale-105 transition-transform duration-300">
                    <span className="text-lg">📎</span>
                  </div>
                  <span className="text-slate-700 font-medium text-sm">
                    {fileList.length > 0 ? `${fileList.length} file(s) selected` : 'Tap to choose files'}
                  </span>
                  {fileList.length > 0 && (
                    <div className="mt-2 p-2 bg-blue-50 rounded-lg">
                      <div className="text-xs text-slate-600">
                        {fileList.slice(0, 2).map((file, index) => (
                          <div key={index} className="truncate">{file.name}</div>
                        ))}
                        {fileList.length > 2 && <div>+{fileList.length - 2} more files</div>}
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </div>

            {/* Relationship Type */}
            <div>
              <label className="block text-sm font-semibold mb-2 text-slate-800">
                Relationship Type
              </label>
              <div className="relative">
                <select
                  value={relationshipType}
                  onChange={(e) => setRelationshipType(e.target.value)}
                  className="appearance-none block w-full px-4 py-3 text-slate-800 bg-white/70 backdrop-blur-sm border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/30 focus:border-blue-500 transition-all duration-300"
                  required
                >
                  <option value="">Select relationship type</option>
                  <option value="romantic">💕 Romantic Partner</option>
                  <option value="spouse">💍 Spouse</option>
                  <option value="dating">🌹 Dating</option>
                  <option value="friend">👥 Friend</option>
                  <option value="family">👨‍👩‍👧‍👦 Family</option>
                  <option value="work">💼 Work</option>
                </select>
                <div className="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                  <svg className="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                  </svg>
                </div>
              </div>
            </div>

            {/* Context */}
            <div>
              <label className="block text-sm font-semibold mb-2 text-slate-800">
                Context <span className="text-red-500">*</span>
              </label>
              <textarea
                value={context}
                onChange={(e) => setContext(e.target.value)}
                rows={3}
                className="block w-full px-4 py-3 text-slate-800 placeholder-slate-400 bg-white/70 backdrop-blur-sm border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/30 focus:border-blue-500 transition-all duration-300 resize-none text-sm"
                placeholder="Describe the conversation context...

e.g., Discussion about trust, argument over boundaries, daily interactions that felt uncomfortable"
                required
              />
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className="relative w-full py-3 rounded-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/30 hover:scale-[1.01] active:scale-[0.99] transition-all duration-300 disabled:opacity-70 disabled:cursor-not-allowed disabled:hover:scale-100 overflow-hidden group"
            >
              {/* Button shine effect */}
              <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
              
              <span className="relative z-10 flex items-center justify-center">
                {loading ? (
                  <>
                    <svg className="animate-spin -ml-1 mr-3 h-6 w-6 text-white" fill="none" viewBox="0 0 24 24">
                      <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" className="opacity-25"></circle>
                      <path fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" className="opacity-75"></path>
                    </svg>
                    Analyzing conversations...
                  </>
                ) : (
                  <>
                    Continue Analysis
                    <svg className="ml-2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                    </svg>
                  </>
                )}
              </span>
            </button>
          </form>
        </div>

        {/* Privacy Notice */}
        <div className="mt-4 p-3 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl border border-blue-100">
          <div className="flex items-center space-x-2">
            <span className="text-blue-600 text-sm">🔒</span>
            <p className="text-xs text-slate-600">
              Your conversations are analyzed privately and securely. Files are deleted after analysis.
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}