export function formatSid(sid: string): string {
  return sid.toUpperCase();
}

export function StudentInformation(props: { classNo: string; name: string; sid: string }) {
  return (
    <p>
      我是{props.classNo}的{props.name}，學號是 <code>{formatSid(props.sid)}</code>。
    </p>
  );
}

export function App() {
  return (
    <div>
      <StudentInformation classNo="智商二甲" name="潘奕濬" sid="c111156103" />
    </div>
  );
}
