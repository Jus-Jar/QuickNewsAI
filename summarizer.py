from openRouter import summarizerAgentRequest

def chunk_content(content, max_chars):
    chunks = []
    for i in range(0, len(content), max_chars):
        chunks.append(content[i:i+max_chars])
    return chunks

def summaryRequest(content,summarizerClient):
    chunks = chunk_content(content,8192)
    summary = []
    
    for chunk in chunks:
        summary.append(summarizerAgentRequest(chunk,summarizerClient))

    mergedSummaries = "".join(summary)

    return summarizerAgentRequest(mergedSummaries,summarizerClient)

    